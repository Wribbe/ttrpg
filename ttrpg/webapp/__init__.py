import bottle

from bottle import run as bottle_run, template, route
from pathlib import Path

@route('/')
def index():
  return template("index", name="World")


def run(host="localhost", port=8080, debug=False):
  """ Our webapp run method. """
  bottle.TEMPLATE_PATH.insert(0, Path("ttrpg", "webapp", "views"))
  bottle_run(host=host, port=port, debug=debug, reloader=debug)
