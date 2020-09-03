import re

import praw
from bot_login import login

def already_replied(comment):
    if not comment.replies:
        return False
    
    for reply in comment.replies:
        if reply.author and reply.author.name == 'thecakeisaliebot':
            return True

    return False


def parse_comments(r):
    count = 0
    for comment in r.subreddit('all').stream.comments():
        if comment.is_root:
            continue
        if re.match('happy cake day', comment.body, re.IGNORECASE):
            return comment
        else:
            count += 1
            print('no match; count: ', count)

if __name__ == '__main__':
    reddit = login()
    
    while True:
        matching_comment = parse_comments(reddit)
