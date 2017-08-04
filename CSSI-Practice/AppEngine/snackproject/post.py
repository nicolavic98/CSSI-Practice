from google.appengine.ext import ndb


from user import User


#jinja_environment = jinja2.Environment(
#    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class Post(ndb.Model):
    image = ndb.BlobProperty()
    description = ndb.StringProperty()
    post_by = ndb.KeyProperty(User)
