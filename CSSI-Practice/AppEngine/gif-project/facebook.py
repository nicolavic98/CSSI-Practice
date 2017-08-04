from google.appengine.ext import ndb
from random import randint
from random import choice



class FacebookPost(ndb.Model):
    username = ndb.StringProperty()
    post_content = ndb.StringProperty()
    num_likes = ndb.IntegerProperty()
    num_reacts = ndb.IntegerProperty()
    num_comments = ndb.IntegerProperty()
