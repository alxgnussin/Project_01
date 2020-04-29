# -*- coding: utf-8 -*-
# Python 3.7.7 required

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def render_index():
    output = render_template('index.html')
    return output


@app.route('/departures/<departure>/')
def render_departure(departure):
    output = render_template('departure.html', departure=departure)
    return output


@app.route('/tours/<id>/')
def render_tour(id):
    output = render_template('tour.html', id=id)
    return output


app.run()
