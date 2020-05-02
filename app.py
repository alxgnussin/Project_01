# -*- coding: utf-8 -*-
# Python 3.7.7 required
from random import randint

from flask import Flask, render_template
from data import tours

app = Flask(__name__)


@app.route("/")
def render_index():
    output = render_template(
        'index.html',
        tours=tours,
        keys=random_generator()
    )
    return output


@app.route('/departures/<departure>/')
def render_departure(departure):
    output = render_template(
        'departure.html',
        my_link=departure,
        keys=departure_select(departure)[0],
        tours=tours,
        price=size(sel_tours=departure_select(departure)[1], select="price"),
        nights=size(sel_tours=departure_select(departure)[1], select="nights"),
        tour_from=departure_from(departure)
    )
    return output


@app.route('/tours/<int:tour_id>/')
def render_tour(tour_id):
    output = render_template(
        'tour.html',
        key=tour_id,
        tour_from=departure_from(tours[tour_id]["departure"]),
        tours=tours
    )
    return output


def departure_from(departure):
    tour_from = 'из Москвы'
    if departure == 'spb':
        tour_from = 'из Петербурга'
    elif departure == 'nsk':
        tour_from = 'из Новосибирска'
    elif departure == 'ekb':
        tour_from = 'из Екатеринбурга'
    elif departure == 'kazan':
        tour_from = 'из Казани'
    return tour_from


def size(sel_tours, select):
    values = []
    for data in sel_tours.values():
        values.append(data[select])
    return values


def departure_select(departure):
    keys = []
    tours_select = {}
    for key, value in tours.items():
        if value['departure'] == departure:
            keys.append(key)
            my_tour = {key: value}
            tours_select.update(my_tour)
    return keys, tours_select


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


if __name__ == '__main__':
    app.run()
