#!/usr/bin/env python

import webapp2
import cgi

"""
Forms

This is the first section of the unit's work. We create a form,
and have it post to a specified url.
"""

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

"""
Validation

This is the second section of the unit's work. We create a form,
asking the user to enter a month, day and year and validate the
submitted data.
"""

form_v="""
<form method="post">
  What is your birthday?
  <br>

  <label> Month
    <input type="text" name="month" value="%(month)s">
  </label>
  <label> Day
    <input type="text" name="day" value="%(day)s">
  </label>
  <label> Year
    <input type="text" name="year" value="%(year)s">
  </label>
  <div style="color: red">%(error)s</div>
  <br>
  <br>
  <input type="submit">
</form>
"""

months = ['January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December']

month_abbrvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
    if month:
        short_month = month[:3].lower()
        if short_month in month_abbrvs:
            return month_abbrvs.get(short_month)

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day in range(1,32):
            return int(day)

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year in range(1900,2021):
            return year

class Validation(webapp2.RequestHandler):
    def write_form(self, month="Month", day="Day", year="Year", error=""):
        self.response.out.write(
                form_v % { "month" : month,
                    "day"   : day,
                    "year"  : year,
                    "error" : error })

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if month and day and year:
            self.response.out.write("Thanks! That's a totally valid day!")
        else:
            self.write_form(user_month, user_day, user_year, "That doesn't look valid to me, friend.")

validation=('/u2/validation', Validation)

"""
String substitution
"""

given_string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
    return given_string2 % (s1, s2)

given_string3 = """I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."""
def sub_m(name, nickname):
    return given_string2 % {"nickname" : nickname,
            "name" : name}


"""
HTML escapipng
"""

escape_dict = {
        ">" : "&gt;",
        "<" : "&lt;",
        "\"" : "&quot;",
        "&" : "&amp;" 
        }

def escape_html_quiz(s):
    for key in escape_dict.keys():
        s = s.replace(key,escape_dict.get(key))
    return s

"""
Alternatively, import the cgi module and use the built-in methods.
Probably smarter to do that.
"""

def escape_html(s):
    return cgi.escape(s, quote = True)

"""
Implement escaping in forms
"""

class ValidateEscape(webapp2.RequestHandler):
    def write_form(self, month="Month", day="Day", year="Year", error=""):
        self.response.out.write(
                form_v % { "month" : escape_html(month),
                    "day"   : escape_html(day),
                    "year"  : escape_html(year),
                    "error" : error })

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if month and day and year:
            self.response.out.write("Thanks! That's a totally valid day!")
        else:
            self.write_form(user_month, user_day, user_year, "That doesn't look valid to me, friend.")

validateescape=('/u2/validateescape', ValidateEscape)

"""
Redirection
"""

class Redirection(webapp2.RequestHandler):
    def write_form(self, month="Month", day="Day", year="Year", error=""):
        self.response.out.write(
                form_v % { "month" : escape_html(month),
                    "day"   : escape_html(day),
                    "year"  : escape_html(year),
                    "error" : error })

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if month and day and year:
            self.redirect("/u2/redirection_end")
        else:
            self.write_form(user_month, user_day, user_year, "That doesn't look valid to me, friend.")

class Thanks(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day!")

redirection_start=('/u2/redirection_start', Redirection)
redirection_end=('/u2/redirection_end', Thanks)

