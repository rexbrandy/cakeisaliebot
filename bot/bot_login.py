import praw

def login():
    r = praw.Reddit('CAKE', user_agent='The cake is a lie bot v1')

    return r