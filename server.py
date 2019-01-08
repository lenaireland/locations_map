"""Location Mapper"""

import os, requests, re

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect
from flask import flash, session, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from bs4 import BeautifulSoup

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

@app.route('/process-url', methods=['GET'])
def url_process():
    """Find locations to map"""

    page_link = request.args.get('url')

    # here, we fetch the content from the url, using the requests library
    page_response = requests.get(page_link, timeout=5)

    #we use the html parser to parse the url content and store it in a variable.
    soup = BeautifulSoup(page_response.content, "html.parser")

    # print(soup)

    out = soup.find_all(text=re.compile("^([^,]+),\s(AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)(?:(\s\d{5}))?$"))

    if out == []:
        out = soup.find_all(text=re.compile("(?:,)([^,]+),\s(AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)\s(?:(\d{5}))?"))  

    # eventually will get rid of these lines and return redirect to mapping page
    # doing this way just for debugging

    print("\n\n\n\n\n\n\nOUTPUT")
    print(out)

    return redirect('/map')
    

@app.route('/map')
def make_map():

    return render_template('map.html', mapbox = mapbox)


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

