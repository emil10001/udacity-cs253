#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import sys
import webapp2
sys.path.append('problem_sets')
import problem1
sys.path.append('units')
import unit2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, Udacity!')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    problem1.main,
    unit2.main,
    unit2.testform
], debug=True)
