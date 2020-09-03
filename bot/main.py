import re

import praw
from bot_login import login

def parse_comments(r):
    count = 0
    for comment in r.subreddit('all').stream.comments():
        if re.match('cake day', comment.body, re.IGNORECASE):
            print(comment.body)
            exit()
        else:
            count += 1
            print('no match; count: ', count)

if __name__ == '__main__':
    reddit = login()
    
    while True:
        parse_comments(reddit)
