"""Location Mapper"""

import os, requests, re

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect
from flask import flash, session, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from bs4 import BeautifulSoup
from mapbox import Geocoder

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = os.environ['SECRET_KEY']

mapbox = os.environ['MAPBOX_KEY']

# AIRNOW = os.environ['AIRNOW_KEY']


# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage - show information about project - take to login"""

    return render_template('homepage.html')

@app.route('/results', methods=['GET'])
def show_results():
    """Find locations to map and send them to map page"""

    page_link = request.args.get('url')

    # here, we fetch the content from the url, using the requests library
    page_response = requests.get(page_link, timeout=5)

    #we use the html parser to parse the url content and store it in a variable.
    soup = BeautifulSoup(page_response.content, "html.parser")

    # print(soup)

    out = soup.find_all(text=re.compile("^([^,]+),\s(AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)(?:(\s\d{5}))?$"))

    if out == []:
        out = soup.find_all(text=re.compile("(?:,)([^,]+),\s(AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)\s(?:(\d{5}))?"))  


    # for debugging
    # print("\n\n\n\n\n\n\nOUTPUT")
    # print(out)

    # Can comment out these lines and uncomment last lines 
    # to dummy out geocode call and save API quota

    # geocoder = Geocoder(access_token=mapbox)

    # for_plotting = []

    # for place in out:

    #     response = geocoder.forward(place, 
    #                                 limit = 1, 
    #                                 country=['us']) 
    #                                 # types=['place'])

    #     first = response.geojson()['features'][0]
    #     # print(first['place_name'])
    #     # print(first['geometry']['coordinates'])

    #     for_plotting.append([first['place_name'], first['geometry']['coordinates']])

    # return render_template('map.html', mapbox = mapbox, places=for_plotting, link=page_link)
    

    # Uncomment these lines to dummy out API call and save quota

    places = ['1105 Hainesport Mount Laurel Rd, Mount Laurel, New Jersey 08054, United States',
              [-74.87109, 39.95182]]

    return render_template('results.html', mapbox=mapbox, places=places, link=page_link)

@app.route('/map')
def map():

    return render_template('map.html')

##############################################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug
    
    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
 
    app.run(port=5000, host='0.0.0.0')
    app.run(debug=True)

