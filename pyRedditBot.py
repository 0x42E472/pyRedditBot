import praw
from time import sleep

# Edit the following options:
usr = "" # Username of Reddit account
pwd = "" # Password of Reddit account
id = "" # ID of Bot
secret = "" # Secret Key of Bot
agent = "" # Custom User Agent (can be whatever you want)
postLimit = 1 # How many posts to search
phrase = "" # The phrase the bot should look for
replyCom = "" # What the bot should reply
subredditCom = "" # Name of subreddit
interval = 0 # How long to wait before checking the subreddit again (in seconds)

print("Logging in...")
reddit = praw.Reddit(client_id=id, client_secret=secret, password=pwd, user_agent=agent, username=usr)
print("Logged in as " + str(reddit.user.me()))

def main():
	trigger = True
	submissions = reddit.subreddit(subredditCom).hot(limit=postLimit) # get hot posts from hot section of subreddit
	for index in submissions:
		commentList = index.comments[0:] # get the comments
		for comment in commentList:
			if (phrase in comment.body): # check if phrase is in comment
				for reply in comment.replies: # go through all replies of the comment
					if (reply.author.name == usr): # check if bot has replied already
						trigger = False
				if (trigger): # if bot has replied already don't comment, otherwise do comment
					comment.reply(replyCom)

while (True):
	main()
	print("Checked. Now waiting " + str(interval) + " seconds.")
	sleep(interval)