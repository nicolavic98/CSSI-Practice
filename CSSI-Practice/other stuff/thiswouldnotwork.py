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
from random import randint

class MainHandler(webapp2.RequestHandler):
    def stuffForPage(self):
        languages = ["Hello, world!", "Hallo, Welt!", "Bonjour, le monde!", "Hola, mundo!", "Ciao, mondo!"]
        number_of_lang = randint(1, len(languages)
        lang_return = []
        for i in range (number_of_lang):
            lang_return.append(languages[i])
        return lang_return
    def get(self):
        response1 = stuffForPage()
        self.response.write(response1)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
