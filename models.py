from google.appengine.ext import ndb
from google.appengine.ext import db

class MovieQuote(ndb.Model):
	quote=ndb.StringProperty()
	movie=ndb.StringProperty()
	last_touch=ndb.DateTimeProperty(auto_now=True)

class User(ndb.Model):
	@classmethod
	def by_name(cls,name):
		qry = User.query(User.username == name).get()
	        return qry
	username=ndb.StringProperty()
	pass_hash=ndb.StringProperty()
	email=ndb.StringProperty()

