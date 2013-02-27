#!/usr/bin/env python

import webapp2

"""
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
This is the second section of the unit's work. We create a form,
asking the user to enter a month, day and year and validate the
submitted data.
"""

form_v="""
<form method="post">
  What is your birthday?
  <br>

  <label> Month
    <input type="text" name="month">
  </label>
  <label> Day
    <input type="text" name="day">
  </label>
  <label> Year
    <input type="text" name="year">
  </label>

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
    def get(self):
        self.response.out.write(form_v)
    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if user_month and user_day and user_year:
            self.response.out.write("Thanks! That's a totally valid day!")
        else:
            self.response.write(form_v)

validation=('/u2/validation', Validation)

