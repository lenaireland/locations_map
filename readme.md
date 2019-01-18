# LocationMapper

LocationMapper is a simple webapp that I created because I was getting ready to travel to a new location in the US and was looking for activities to do while there.  Unfortunately, the websites I found simply listed attractions with an address or city, state.  As I was unfamiliar with the geography of the area, I found myself entering locations one-by-one into an online map, only to find most of the listed attractions were too far away from where I was staying.  So, I created this tool to map all the listed locations at once to save my time and sanity.  It's a simple tool that uses regex to find locations to map (which is currently not very robust)... but it worked for my use and maybe you can adapt it for yours too!

## Table of Contents

* [Tech Stack](#tech-stack)
* [Features](#features)
* [Setup/Installation](#installation)
* [About Me](#aboutme)

## <a name="tech-stack"></a>Tech Stack

__Backend:__ Python, Flask, BeautifulSoup <br/>
__Frontend:__ JavaScript, Jinja2, Bootstrap, HTML5, CSS3 <br/>
__API:__ Mapbox <br/>

## <a name="features"></a>Features

This is a simple little webapp that scrapes a webpage using BeautifulSoup and returns a new page with side-by-side iframes of the original webpage and a map showing any US locations recognized on the original webpage.

## <a name="installation"></a>Setup/Installation

#### Requirements:

- Python 3.6
- Mapbox API key

To have this app running on your local computer, please follow the below steps:

Clone or fork this repository:
```
$ git clone https://github.com/lenaireland/locations_map.git
```

Create a virtual environment inside your locations_map directory:
```
$ virtualenv env
```

Activate the virtual environment:
```
$ source env/bin/activate
```

Install dependencies:
```
$ pip3 install -r requirements.txt
```

Sign up to use the [Mapbox API](https://www.mapbox.com/signup/) and obtain an API key. Save it to a file `secrets.sh`, along with a secret key you choose for the app. Your file should look something like this:
```
export SECRET_KEY = 'xyz'
export MAPBOX_KEY= = 'abc'
```

Source your keys from your `secrets.sh` file into your virtual environment:
```
$ source secrets.sh
```

Run the app from the command line.
```
$ python3 server.py
```

You can now navigate to 'localhost:5000/' to access LocationMapper.

## <a name="aboutme"></a>About Me
Lena Ireland is a Software Engineer in the Bay Area; this was a quick side project to make her life easier.
Visit her on [LinkedIn](http://www.linkedin.com/in/lenaireland).