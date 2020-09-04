import praw
import os

def login():
    r = praw.Reddit(
        username = os.environ["reddit_username"],
        password = os.environ["reddit_password"],
        client_id = os.environ["client_id"],
        client_secret = os.environ["client_secret"],
        user_agent='The cake is a lie bot v1, Github: https://github.com/rexbrandy/cakeisaliebot'
    )

    return r