import os
import sys
import configparser
from makeimage import makeImage,makeImages
from readtweets import gettweets
from Queue import Queue
import subprocess
from keys  import getkeys
from flask import Flask
app = Flask(__name__)

@app.route('/starthere/<keyword>')
def word2vid(keyword):
	keys = getkeys()
	consumer_key = keys[0]
	consumer_secret = keys[1]
	access_key = keys[2]
	access_secret = keys[3]

	line = keyword
	words = line.split(',')
	q = Queue(words)
	video_num = 0
	print(q.isEmpty())
	print(q.length())
	while not q.isEmpty():
		word = q.items[0]
		image0 = "images/"+ str(video_num) + "-%01d.png"
		video = word+".avi"
		tweets = gettweets(word,consumer_key,consumer_secret,access_key,access_secret)
		makeImages(video_num,tweets)
		video_num = video_num+1
		subprocess.call(['ffmpeg','-y', '-framerate', '.1', '-i', image0, video])
		q.queuedown()
	return keyword

def main(keyword = "Boston University,ECE"):
	word2vid(keyword)
	return keyword

if __name__ == '__main__':
	main()

