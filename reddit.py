import praw

reddit = praw.Reddit(client_id='Ipmh7JRwQcNMNA',
                         client_secret="7lhfK2BGbidMt3X8nFDAc2fk5qo",
                         user_agent='prawtutorialV1')

eyebleach = reddit.subreddit("eyebleach")
hot_eye = eyebleach.hot(limit=5)
posts = []
for submission in hot_eye:
    posts.append(submission.url)

print(posts)
