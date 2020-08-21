from flask import Flask, render_template, request, jsonify, Markup,send_file
import flask_restful
import configparser
import json
from hw4 import word2vid

app = Flask(__name__)
api = flask_restful.Api(app)
base_url = '127.0.0.1:5000'

@app.route('/get_status/<string:keyword>',methods=['GET'])
def get_status(keyword):
    if keyword in app.mykeyword:
        if app.mykeyword[keyword] == 1:
            status = 'Ready'
        else:
            status = 'Still working on it'
    else:
        status = 'Keyword is not exist'
    
    return jsonify(keyword=keyword,
                    status=status,)




@app.route('/get_video/<string:keyword>',methods=['GET'])
def get_video(keyword):
    try:
        return send_file(keyword+'.avi')
    except:
        print("cant send file, maybe the file isnt exist")
        return flask_restful.abort(404, message="keyword doesn't exist")


@app.route('/make_video/<string:keyword>',methods=['GET'])
def make_video(keyword):
    status_link = ''
    video_link = ''
    app.mykeyword[keyword] = 1
    rtn = word2vid(keyword)
    app.mykeyword[keyword] = 2
    status_link = base_url + '/get_status/' + keyword
    video_link = base_url + '/get_video/' + keyword
    return jsonify(keyword=keyword,
                get_status=status_link,
                get_video=video_link )


@app.route('/', methods=['POST'])
def post():
    status_link = ''
    video_link = ''
    keyword = request.form['keyword']
    app.mykeyword[keyword] = 1
    rtn = word2vid(keyword)
    app.mykeyword[keyword] = 2
    status_link = base_url + '/get_status/' + keyword
    video_link = base_url + '/get_video/' + keyword
    
    return jsonify(keyword=keyword,
                get_status=status_link,
                get_video=video_link )




if __name__ == "__main__":
    app.mykeyword = dict()
    app.run(debug=True)
    #app.run(debug=True,host='0.0.0.0',port=8080)