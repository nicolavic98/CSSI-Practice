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

import jinja2
import os
import webapp2
from random import randint

#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def stuffForPage(self):
        languages = ["Hello, world!", "Hallo, Welt!", "Bonjour, le monde!", "Hola, mundo!", "Ciao, mondo!",]
        return languages[randint(0, len(languages)-1)]
    def get(self):
        response = self.stuffForPage()
        self.response.write(response)

class ColorHandler(webapp2.RequestHandler):
    def get(self):
        color_name = str(self.request.get("color"))
        number = int(self.request.get("number"))
        list_ohno = []
        for i in range(number):
            list_ohno.append(color_name)
            self.response.write("Yay! " + color_name+ " <br>")

class ImageHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template("templates/hello_world.html")
        #you could also do render_data {"name" = self.request.get("varname")}
        my_name = self.request.get("my_name")
        favorite_color = self.request.get("favorite_color")
        a_number = int(self.request.get("a_number"))
        #my_favorite_color = self.request.get("favorite_color")
        render_data = { 'greeting': "Hello"}
        render_data["name"] = my_name
        render_data["color"] = favorite_color
        render_data["a_number"] = a_number
        if my_name == "":
            render_data["name"] = "person"
        self.response.write(my_template.render(render_data))
        #self.response.write("<link rel='stylesheet' href='resources/appstuff.css'>")
        #self.response.write("<h1><i>")
        #self.response.write("My Handler Worked")
        #self.response.write("</i></h1>")
        #self.response.write("<img src=/resources/unitato.jpg>")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/color', ColorHandler),
    ('/image', ImageHandler),
], debug=True)
