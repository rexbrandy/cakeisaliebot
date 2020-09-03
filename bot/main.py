import re
import time

import praw
from bot_login import login
from config import BLACKLISTED_SUBS

BANNED_SUBS = []

def allowed_to_post(target_sub):
    if target_sub in BLACKLISTED_SUBS or target_sub in BANNED_SUBS:
        return False
    return True

def reply_to_comment(comment):
    reply_text = 'The cake is a lie'
    if allowed_to_post(comment.subreddit):
        try:
            comment.reply(reply_text)
            print('Replied, comment.id: ', comment.id)
        except Exception as e:
            print("REPLY FAILED: %s @ %s"%(e, comment.subreddit))
            if str(e) == '403 Client Error: Forbidden':
                BANNED_SUBS.append(comment.subreddit)

def already_replied(comment):
    if not comment.replies:
        return False
    for reply in comment.replies:
        if reply.author and reply.author.name == 'thecakeisaliebot':
            return True
    return False


def parse_comments(r):
    for comment in r.subreddit('all').stream.comments():
        if comment.is_root:
            continue
        elif re.match('happy cake day', comment.body, re.IGNORECASE):
            return comment


def run():
    reddit = login()
    
    while True:
        matching_comment = parse_comments(reddit)

        if not already_replied(matching_comment):
            reply_to_comment(matching_comment)

            time.sleep(300)

