#!/usr/bin/env python3

from ttrpg import webapp

def main():
  """ Main runner for the ttrpg project. """
  webapp.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == "__main__":
  main()
