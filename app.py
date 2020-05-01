# -*- coding: utf-8 -*-
# Python 3.7.7 required
from random import randint

from flask import Flask, render_template
from data import tours

app = Flask(__name__)


@app.route("/")
def render_index():
    output = render_template('index.html', tours=tours, keys=random_generator())
    return output


@app.route('/departures/<departure>/')
def render_departure(departure):
    output = render_template('departure.html', my_link=departure, tours=tours, price=size("price"),
                             nights=size("nights"), keys=departure_select(departure))
    return output


@app.route('/tours/<int:tour_id>/')
def render_tour(tour_id):
    if tours[tour_id]["departure"] == 'msk':
        tour_from = 'Из Москвы'
    elif tours[tour_id]["departure"] == 'spb':
        tour_from = 'Из Петербурга'
    elif tours[tour_id]["departure"] == 'nsk':
        tour_from = 'Из Новосибирска'
    elif tours[tour_id]["departure"] == 'ekb':
        tour_from = 'Из Екатеринбурга'
    elif tours[tour_id]["departure"] == 'kazan':
        tour_from = 'Из Казани'

    output = render_template('tour.html', key=tour_id, tour_from=tour_from, tours=tours)
    return output


def size(key):
    values = []
    for data in tours.values():
        values.append(data[key])
    return values


def departure_select(departure):
    keys = []
    for key, value in tours.items():
        if value['departure'] == departure:
            keys.append(key)
    return random_generator(tour_id=keys)


def random_generator(tour_id=None):
    if tour_id is None:
        keys = []
    else:
        keys = tour_id
    while len(keys) < 6:
        key = randint(1, len(tours))
        if key in keys:
            continue
        else:
            keys.append(key)
    return keys


app.run()
