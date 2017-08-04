from google.appengine.ext import ndb



#kind string
#rating integer
#quantity integer
#calories integer
#expiration date

#images =blobproperty


class Snack(ndb.Model):
    kind = ndb.StringProperty(required = True)
    rating = ndb.IntegerProperty(repeated = True) #repeated allows you to have multiple things. like multiple posts
    quantity = ndb.IntegerProperty()
    calories = ndb.IntegerProperty()
    expiration = ndb.DateProperty()
