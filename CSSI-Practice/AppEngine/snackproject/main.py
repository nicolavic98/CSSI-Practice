from google.appengine.ext import ndb
import webapp2
import jinja2
import os
from snack import Snack
import urllib2
import urllib
import json

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
# key property lets you access one model from within another
#kind string
#rating integer
#quantity integer
#calories integer
#expiration date
#images =blobproperty

class MainHandler(webapp2.RequestHandler):
    def get(self):
        snack_kind = self.request.get("kind")
        my_template = jinja_environment.get_template('templates/snack.html')
        render_data = {}
        render_data["kind"] = snack_kind
        self.response.write(my_template.render(render_data))
        my_snack = Snack(kind = snack_kind)
        my_snack.put()

        #snack_rating = int(self.request.get("rating"))
        #snack_quantity = int(self.request.get("quantity"))
        #snack_calories = int(self.request.get("calories"))
        #snack_expiration = self.request.get("expiration")
class DisplaySnacksHandler(webapp2.RequestHandler):
     def get(self):
        new_template = jinja_environment.get_template('templates/display.html')
        query = Snack.query()
        render_data = {}
        render_data['snack_list'] = query.fetch()
        self.response.write(new_template.render(render_data))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/snacko', DisplaySnacksHandler),
], debug=True)
