#!/usr/bin/env python

import webapp2
import string
import cgi

"""
ROT 13

rotate each letter by 13 characters, and wrap

Preserve case, white space and punctuation. Re-submitting text should
bring us back to normal. Input text should be escaped.
"""

rot13form="""
<h1>ROT13 some text!</h1>
<br>
<form method="post">
  <textarea name="text" style="height: 100px; width: 400px;">%(rotten)s</textarea>
  <br>
  <input type="submit">
</form>
"""


def rot13(s):
    s2=""
    for c in s:
        if c in string.ascii_lowercase:
            s2 += chr((( ord(c) - ord("a") + 13 ) % 26 ) + ord("a"))
        elif c in string.ascii_uppercase:
            s2 += chr((( ord(c) - ord("A") + 13 ) % 26 ) + ord("A"))
        else:
            s2 += c
    return s2

class ROT13Handler(webapp2.RequestHandler):
    def write_form(self, rotten=""):
        self.response.out.write(rot13form % { "rotten" : rotten })

    def get(self):
        self.write_form()
    def post(self):
        user_rotten = rot13( self.request.get('text') )
        user_rotten = cgi.escape( user_rotten, quote = True )
        self.write_form(user_rotten)

rot13page=('/ps2/rot13', ROT13Handler)


class SignupHandler(webapp2.RequestHandler):

signuppage=('/ps2/signup', SignupHandler)
