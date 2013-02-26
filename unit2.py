#!/usr/bin/env python

import webapp2

form="""
<form method="post" action="/u2/testform">
  <input name="q">
  <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
    def get(self):
        q = self.request.get("q")
        self.response.out.write(q)
        # Uncomment to see the raw request
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write(self.request)
    def post(self):
        q = self.request.get("q")
        self.response.out.write(q)

main=('/u2', MainHandler)
testform=('/u2/testform', TestHandler)

