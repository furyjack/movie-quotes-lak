from google.appengine.ext import ndb

class MovieQuote(ndb.Model):
	quote=ndb.StringProperty()
	movie=ndb.StringProperty()
	last_touch=ndb.DateTimeProperty(auto_now=True)


