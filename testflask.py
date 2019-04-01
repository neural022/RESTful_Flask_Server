# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:10:55 2019

@author: KAO
"""

from flask import Flask
#return json format
from flask import jsonify
#return error 404
from flask import make_response
#Client request
#from flask import request
#WSGI combine Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/Service/get', methods=['GET'])
def get_Hello():
    hello = [{ 'hello':'Hello World!'}]
    print("Response:" + str(hello))
    return jsonify(hello)

@app.route('/Service/get/<string:sentence>', methods=['GET'])
def get_String(sentence):
    s = [{'sentence':'我很好'}, {'sentence2':'那你呢'}]
    s2 = [{'sentence':'問號'}]
    print("Request:" + str(sentence))
    if sentence == "你好嗎":
        print("Response:" + str(s))
        return jsonify(s)
    else:
        print("Response:" + str(s2))
        return jsonify(s2)

@app.route('/Service/post/<int:num>', methods=['POST'])
def post_Num(num):
    value1 = [{'value': '1'}, {'value': '2'}]
    value2 = [{'value': '3'}, {'value': '4'}]
    print("request: " + str(num))
    if num == 1 or num == 2:
        return jsonify(value1)
    elif num == 3 or num == 4:
        return jsonify(value2)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=5000, debug=True)
    print("Server running...")
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()
    