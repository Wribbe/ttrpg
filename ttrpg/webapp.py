from bottle import run as bottle_run, template, route

@route('/')
def index():
  return "<h1>Hello World!</h1>"

def run(host="localhost", port=8080, debug=False):
  """ Our webapp run method. """
  bottle_run(host=host, port=port, debug=debug, reloader=debug)
