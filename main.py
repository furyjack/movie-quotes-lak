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
import random
import string
import hashlib
import hmac
from models import MovieQuote
from models import User
from google.appengine.ext import ndb
template_dir= os.path.join(os.path.dirname(__file__),'templates')
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)
secret="blablabla"

def make_secure_val(val):
	return val + '|' + hmac.new(secret,val).hexdigest()

def check_secure_val(secure_val):
	val=secure_val.split('|')[0]
	if secure_val==make_secure_val(val):
		return val


class Handler(webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)
    def render_str(self,template,**params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self,template,**kw):
        self.write(self.render_str(template,**kw))
    PARENT_KEY=ndb.Key("MovieQuotes","root")
    def set_cookie(self,name,val):
    	#check last line possible error
    	cookie_val=make_secure_val(val)
    	cookie_val=str(cookie_val)
    	self.response.headers.add_header('Set-Cookie','%s=%s' % (name,cookie_val),path='/')

    def read_cookie(self,name):
    	cookie_val=self.request.cookies.get(name)
    	if cookie_val == None:
    		return None
    	else:
    	    return cookie_val.split('|')[0] and check_secure_val(cookie_val)

    def make_salt(self):
          return ''.join(random.choice(string.letters) for i in range(5))
	
    def make_pw_hash(self,name, pw,salt=None):
         if not salt:
          salt=self.make_salt()
         s=hashlib.sha256(name+pw+salt).hexdigest() +'|'+salt
         return s

    def valid_pw(self,name,pw,h):
	salt=h.split('|')[1]
	return h==self.make_pw_hash(name,pw,salt)


class WelcomePage(Handler):
	def get(self):
		self.render('Welcome_Page.html')

class MainHandler(Handler):
    def get(self):
    	moviequotes=MovieQuote.query(ancestor=self.PARENT_KEY).order(-MovieQuote.last_touch)
    	u=self.read_cookie('user')
    	exist=self.read_cookie('exist')
    	if u==None:
    	    if exist == 'true':
            	self.render('moviequotes.html',moviequotes=moviequotes,user="",error="true")
            elif exist=='wrong':
            	self.render('moviequotes.html',moviequotes=moviequotes,user="",error="wrong")
            else:
            	self.render('moviequotes.html',moviequotes=moviequotes,user="",error="false")
    		
        else:
            if exist=='true':
            	self.render('moviequotes.html',moviequotes=moviequotes,user=u,error="true")
            elif exist=='wrong':
            	self.render('moviequotes.html',moviequotes=moviequotes,user="",error="wrong")
            else:
            	self.render('moviequotes.html',moviequotes=moviequotes,user=u,error="false")
        self.set_cookie('exist','false')

class AddQuoteAction(Handler):
    def post(self):
    	if self.request.get('entity-key'):
    		movie_quote_key=ndb.Key(urlsafe=self.request.get('entity-key'))
    		instance=movie_quote_key.get()
    		instance.quote=self.request.get('quote')
    		instance.movie=self.request.get('movie')
    		instance.put()
    	else:
	        quote=self.request.get('quote')
	        movie=self.request.get('movie')
	        new_movie_quote=MovieQuote(parent=self.PARENT_KEY,quote=quote,movie=movie)
	        new_movie_quote.put()
        self.redirect(self.request.referer)

class SignUpHandler(Handler):

	
	def post(self):
	    Username=self.request.get('username')
	    user_exist=User.by_name(Username)
	    if not user_exist:
	    	Password=self.request.get('password')
	    	Con_Password=self.request.get('c_password')
	    	Email=self.request.get('email')
	    	pw_hash=self.make_pw_hash(Username,Password,None)
	    	U=User(username=Username,pass_hash=pw_hash,email=Email)
	    	U.put()
	    	self.set_cookie('user',Username)
	    	self.set_cookie('exist',"false")
	    else:
	    	self.set_cookie('exist',"true")
	    self.redirect(self.request.referer)
	   
class LogInHandler(Handler):

	def post(self):
	    Username=self.request.get('username')
	    Password=self.request.get('password')
	    u=User.by_name(Username)
	    if u and self.valid_pw(Username,Password,u.pass_hash):
	       self.set_cookie('user',Username)
	    else:
	    	self.set_cookie('exist','wrong')
	    self.redirect(self.request.referer)

class LogOutHandler(Handler):
	def get(self):
		self.response.headers.add_header('Set-Cookie','user=',path='/')
		self.redirect('/')
		
		

class DelQuoteAction(Handler):
    def post(self):
    	if self.request.get('entity-key-del'):
    		movie_quote_key=ndb.Key(urlsafe=self.request.get('entity-key-del'))
    	        movie_quote_key.delete()
        self.redirect(self.request.referer)



app = webapp2.WSGIApplication([
    ('/', MainHandler),('/addquote',AddQuoteAction),('/delquote',DelQuoteAction),('/signup',SignUpHandler),('/login',LogInHandler),('/logout',LogOutHandler)
], debug=True)
