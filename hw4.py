import os
import sys
import configparser
from makeimage import makeImage,makeImages
from readtweets import gettweets
import subprocess
from keys  import getkeys
from flask import Flask


def word2vid(keyword):
	keys = getkeys()
	consumer_key = keys[0]
	consumer_secret = keys[1]
	access_key = keys[2]
	access_secret = keys[3]


	image0 = "images/"+ str(keyword) + "-%01d.png"
	video = keyword+".avi"
	tweets = gettweets(keyword,consumer_key,consumer_secret,access_key,access_secret)
	makeImages(keyword,tweets)
	subprocess.call(['ffmpeg','-y', '-framerate', '.1', '-i', image0, video])

	return keyword

def main(keyword = "obama"):
	word2vid(keyword)
	return keyword

if __name__ == '__main__':
	main()

