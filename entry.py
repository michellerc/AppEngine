#!/usr/bin/env/python

import os
import webapp2
import jethro.page.handlers

_IS_DEBUG = True

_WEBAPP_CONFIG = {
    'webapp2_extras.jinja2': { 
        'template_path': os.path.join(os.path.dirname(__file__), "static", "templates"),
        'environment_args' : {
            'auto_reload' : _IS_DEBUG
        }
    }
}

#class MainHandler(webapp2.RequestHandler):
#   def get(self):
#        self.response.write("hello!")

frontend_app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/albums', jethro.page.handlers.AlbumPageHandler)
    ], config =_WEBAPP_CONFIG, debug=_IS_DEBUG)