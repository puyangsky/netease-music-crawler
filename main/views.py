#!/usr/bin/env python
# encoding: utf-8

"""
@author: puyangsky
@file: views.py
@time: 2018/6/2 上午12:55
"""

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/test')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    return render_template("index.html",
                           title="NetEase Music Crawler")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)