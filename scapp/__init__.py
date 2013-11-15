#!/usr/bin/env python
#coding=utf-8
from functools import wraps
from flask import Flask, render_template, g ,request,session,redirect, url_for

from scapp.views import index
from scapp.views import information
from scapp.views import process
from scapp.views import system
from scapp.views import report

from scapp.extensions import db

app = Flask(__name__)

#app.config.from_object('scapp.config.DevConfig') # sqlite
app.config.from_object('scapp.config.ProConfig') # mysql

app.register_module(index)
app.register_module(information)
app.register_module(process)
app.register_module(system)
app.register_module(report)

db.init_app(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', error = error), 404
	
@app.errorhandler(500)
def page_not_found(error):
    return render_template('errors/500.html', error = error), 500

