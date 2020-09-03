import praw

r = praw.Reddit('CAKE', user_agent='The cake is a lie bot v1')

print(r.read_only)