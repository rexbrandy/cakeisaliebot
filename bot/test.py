import praw
from pprint import pprint

r = praw.Reddit('CAKE', user_agent='The cake is a lie bot v1')

for comment in r.subreddit('all').stream.comments():
    pprint(vars(comment))
    if comment.parent_id:
        parent = comment.parent()
        par_comm = parent.body
        print(par_comm)
        exit()