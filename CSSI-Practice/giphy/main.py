import jinja2
import json
import os
import webapp2
import urllib
import urllib2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/giphy.html")
        #render_data = {"image_url": "https://vignette1.wikia.nocookie.net/trollpasta/images/5/5e/Uniato.jpg/revision/latest/scale-to-width-down/180?cb=20130614202202"}
        query = self.request.get("search")
        index = int(self.request.get("index"))
        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': query, 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        request_url = base_url + urllib.urlencode(url_params)
        giphy_response = urllib2.urlopen(request_url)
        #    "http://api.giphy.com/v1/gifs/search?q=kittens&api_key=dc6zaTOxFJmzC&limit=10")
        giphy_json = giphy_response.read()
        giphy_data = json.loads(giphy_json)
        giphy_url =giphy_data['data'][5]["images"]['original']['url']
        render_data = {}
        render_data['image_url'] = giphy_url
        self.response.write(template.render(render_data))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
