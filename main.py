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
import jinja2
import os
import logging
from models import MovieQuote
from google.appengine.ext import ndb
template_dir= os.path.join(os.path.dirname(__file__),'templates')
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)



class Handler(webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)
    def render_str(self,template,**params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self,template,**kw):
        self.write(self.render_str(template,**kw))
    PARENT_KEY=ndb.Key("MovieQuotes","root")

class MainHandler(Handler):
    def get(self):
    	moviequotes=MovieQuote.query(ancestor=self.PARENT_KEY).order(-MovieQuote.last_touch)
        self.render('moviequotes.html',moviequotes=moviequotes)

class AddQuoteAction(Handler):
    def post(self):
        quote=self.request.get('quote')
        movie=self.request.get('movie')
        new_movie_quote=MovieQuote(parent=self.PARENT_KEY,quote=quote,movie=movie)
        new_movie_quote.put()
        self.redirect(self.request.referer)

app = webapp2.WSGIApplication([
    ('/', MainHandler),('/addquote',AddQuoteAction)
], debug=True)
