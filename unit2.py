#!/usr/bin/env python

import webapp2

form="""
<form action="http://www.google.com/search">
  <input name="q">
  <input type="submit">
</form>
"""

class UnitTwoHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

