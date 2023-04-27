""" A set of python functions for the index page.

A set of functions to manipulate the DOM and add some interactivity
to the home page."""

# imports
import json
from pyodide.ffi import create_proxy
from js import document
from js import window


# get the project data as a dict
@create_proxy
def load_content(*args):
    with open('project_data.json') as f:
        data = json.load(f)
    projects = data.get('projects')
    menu = create_menu(projects)
    document.getElementById('hello').innerHTML = menu

def create_menu(projects):
    menu = "<ul>"
    for project in projects:
        title = project.get("project_title")
        href = project.get("project_dir")
        href += project.get("project_filename")
        description = project.get("project_description")
        li = '<li><a href="' + href + '">' + title + '</a></li>'
        menu += li 
    menu += "</ul>"
    return menu
    

load_content()