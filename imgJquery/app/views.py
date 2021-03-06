# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request
from app import app

@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/_imgClick')
def imgClick():
    x = request.args.get('x', 0, type=float)
    y = request.args.get('y', 0, type=float)
    return jsonify(result=x + y/1000)


@app.route('/')
def index():
	imgData = open('/home/pboord/Downloads/yelp/waitrose.jpg', 'rb').read().encode('base64').replace('\n', '')
	return render_template('index.html', imgData = imgData)

if __name__ == '__main__':
    app.run()
