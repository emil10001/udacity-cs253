#!/usr/bin/env python

import webapp2

class PSOneHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, Udacity!')

main=('/ps1', PSOneHandler)
