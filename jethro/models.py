from google.appengine.ext import ndb

class Artist(ndb.Model):
  name = ndb.StringProperty()
  origin = ndb.StringProperty()

class Album(ndb.Model):
  name = ndb.StringProperty()
  origin = ndb.StringProperty()

class Artist(ndb.Model):
  name = ndb.StringProperty()
  origin = ndb.StringProperty()

class Song(ndb.Model):
  name = ndb.StringProperty()
  origin = ndb.StringProperty()
