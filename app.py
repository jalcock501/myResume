#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created By: jalco on 25/08/2020
import flask
from views import home_views

app = flask.Flask(__name__)
app.register_blueprint(home_views.blueprint)


if __name__ == '__main__':
    app.run(debug=False)
