""" A set of python functions for the index page.

A set of functions to manipulate the DOM and add some interactivity
to the home page."""

# imports
import json
from pyodide.ffi import create_proxy
from js import document


# get the project data as a dict
@create_proxy
def load_content(*args):
    with open('project_data.json') as f:
        data = json.load(f)
    document.getElementById('hello').innerHTML = data['projects'][0].get("project_title")
    
document.getElementById('load_btn').addEventListener('click', load_content)    

