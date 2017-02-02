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
import webapp2
import re

def build_page(content):
    form = """<form method='post'>
    <h1>SIGNUP</h1><br>
    <label>Username: <input type='text' name='usr_name'></input></label><br>
    <label>Password: <input type='password' name='pass'></input></label><br>
    <label>Confirm Password: <input type='password' name='pass_confirm'></input></label><br>
    <label>Email (Optional): <input type='text' name='email'></input></label><br>
    <input type='submit'><br>
    </form>"""
    return form

def error_page_usr(content):
    form = """<form method='post'>
    <h1>SIGNUP</h1><br>
    <label>Username: <input type='text' name='usr_name'></input>Your Username is invalid</label><br>
    <label>Password: <input type='password' name='pass'></input></label><br>
    <label>Confirm Password: <input type='password' name='pass_confirm'></input></label><br>
    <label>Email (Optional): <input type='text' name='email'></input></label><br>
    <input type='submit'><br>
    </form>"""
    return form

def error_page_pass(content):
    form = """<form method='post'>
    <h1>SIGNUP</h1><br>
    <label>Username: <input type='text' name='usr_name'></input></label><br>
    <label>Password: <input type='password' name='pass'></input>Your Password is invalid %s</label><br>
    <label>Confirm Password: <input type='password' name='pass_confirm'></input></label><br>
    <label>Email (Optional): <input type='text' name='email'></input></label><br>
    <input type='submit'><br>
    </form>"""
    return form

usr_test = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
pass_test = re.compile(r"^.{3,20}$")
#email_test = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def val_usr(username):
    return username and usr_test.match(username)

def val_pass(password):
    return password and pass_test.match(password)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        form = build_page("")
        return self.response.write(form)

    def post(self):
        username = self.request.get("usr_name")
        welcome = "<h1>Welcome, " + username + "!</h1>"
        password = self.request.get("pass")
        #confirm_password = self.request.get("pass_confirm")
        #email = self.request.get("email")
        if not val_usr(username):
            usr_err = error_page_usr("")
            return self.response.write(usr_err)
        else:
            return self.response.write(welcome)

        if not val_pass(password):
            pass_err = error_page_pass("")
            return self.response.write(pass_err % test)
        else:
            return self.response.write(welcome)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
