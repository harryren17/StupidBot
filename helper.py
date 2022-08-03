import praw
import random
from os import environ
from dotenv import load_dotenv

load_dotenv()
PASSWORD = environ["PASSWORD"]
SECRET = environ["SECRET"]
secretsauce = environ["SECRETSAUCE"]
saucelimit = 200

reddit = praw.Reddit(client_id='USq-V1BgU2mDhE8Ladv43w', client_secret = SECRET, user_agent = 'stupid-bot', username='stupidbottyboy', password=PASSWORD)
sources = [secretsauce, "shitposting"]

def isValidImage(submission):
    return submission.is_se

def getImageLink():
    posts = list((reddit.subreddit(random.choice(sources))).hot(limit=saucelimit))
    # this is a first draft, we will need to fix this
    submission = random.choice(posts)
    while (submission.url[8:17] != "i.redd.it"):
        submission = random.choice(posts)
    return submission.url

def getRandomCaption():
    posts = list((reddit.subreddit(random.choice(sources))).hot(limit=saucelimit))
    # this is a first draft, we will need to fix this
    submission = random.choice(posts)
    return submission.title