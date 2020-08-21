# HW5: twitter-summarizer-rest-service-chijunyou

In this homework, I deployed my HW4 to AWS EC2.

## Files
hw4.py : a file with word2vid function which can get a keyword, get twitter feeds and make a video
Queue.py : a queue system can make videos synchronously and the max number of threads is 10
keys.py : read keys from keys file
makeimage.py : make images from twitter feeds.
HW5rest.py : file with flask function.

## HW5rest Functions:
get_status(keyword): it can be use with path(/get_status/<keyword>) and can return the status of a keyword in a json file.
get_video(keyword): it can be use with path(/get_video/<keyword>) and can return the video file.
make_video(keyword): it can be use with path(/make_video/<keyword>) and can make a video for a keyword.
post(): it can be used in terminal with special command 'curl -X POST -d "keyword=<keyword>" http://ec2-18-219-96-248.us-east-2.compute.amazonaws.com:8080/' to make a video for a keyword
  
## How to use:
Everyone can reach this by using browser

* First: visit 'http://ec2-18-219-96-248.us-east-2.compute.amazonaws.com:8080/make_video/keyword' to generate a twitter-summarized-video.
* Optional: use command 'curl -X POST -d "keyword=<keyword>" http://ec2-18-219-96-248.us-east-2.compute.amazonaws.com:8080/' to make the video.
  
  
* Second: visit 'http://ec2-18-219-96-248.us-east-2.compute.amazonaws.com:8080/get_status/keyword' to check the status of the video.
* Opional: use command 'curl http://ec2-3-133-92-223.us-east-2.compute.amazonaws.com:8080/status/covid19' to  check the status.


* Third: visit 'http://ec2-18-219-96-248.us-east-2.compute.amazonaws.com:8080/get_video/keyword' to download the video made.

## The way to deploy a local version:
* First: use 'pip install -r requirements' to install prerequest modules.
* Second: run 'python HW5rest_local.py'
* Third: open a browser and visit 'http://127.0.0.1:5000/make_video/<keyword>'to generate a video and visit 'http://127.0.0.1:5000/get_video/<keyword>' to view the video.
  
  

## Result
EC2 server result:
![Image text](https://github.com/BUEC500C1/twitter-summarizer-rest-service-chijunyou/blob/master/putty.png)
Using local terminal to reach the flask deployed on EC2 server:
![Image text](https://github.com/BUEC500C1/twitter-summarizer-rest-service-chijunyou/blob/master/localterminal.png)
