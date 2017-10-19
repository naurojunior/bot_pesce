import config
import praw
import time
import os
import random

def bot_login():
	print ("Loggin...")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = config.user_agent)
	print ("Logged in")
	return r

def run_bot(r, comments_replied):
	word = ""
	
	for comment in r.subreddit('test').comments(limit=25):
		if any(word in comment.body for word in config.palavras_chave) and comment.id not in comments_replied: # and comment.author != r.user.me():
			print ("Comment found")
			#comment.reply("")
			print ("Replied: " + get_reply())
			comments_replied.append(comment.id)
			
			with open("comments_replied.txt", "a") as fw:
				fw.write(comment.id + ",")
			
def load_comments():
	comments_replied = []
	
	if os.path.isfile("comments_replied.txt"):
		with open("comments_replied.txt", "r") as fr: 
			comments_replied = fr.read().split(",")
			comments_replied = list(filter(None, comments_replied))
		
	return comments_replied

	
def get_diplomas():
	qnt_diplomas = random.randrange(1,len(config.diplomas) + 1)
	diploma_quotation = ""
	random.shuffle(config.diplomas)
	
	for x in range(0, qnt_diplomas):
		diploma_quotation += config.diplomas[x] + "\n"
	
	return diploma_quotation
	
def get_effect_phrase():
	return config.replies[random.randrange(0,len(config.replies))]

def get_reply():
	return get_effect_phrase() + "\n" + get_diplomas()

print (get_diplomas())
#print (config.respostas[random.randrange(0,len(config.respostas))])

r = bot_login()
#while True:
run_bot(r, load_comments())
	#time.sleep(10)

					 
