#console for data store stuff (connect to facebook.py)



from facebook import FacebookPost
from main import MainHandler
from random import randint
from random import choice


post = FacebookPost(username = "nvjarmula", post_content = "Going on a trip!", num_likes = randint(0,100), num_reacts = randint(0,100), num_comments = randint(0,100))

query = FacebookPost.query()

post.put()


for i in range(15):
    print query.fetch()[1].num_reacts
    print query.fetch()[1].num_comments
