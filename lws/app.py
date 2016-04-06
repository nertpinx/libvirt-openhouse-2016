# -*- coding: utf-8 -*-
import os

import libvirt

from flask import Flask, render_template, request, jsonify
from . import config
from .helpers import state_str

app = Flask(__name__)
app.config.from_object(config)

conn = libvirt.open()

@app.route('/')
def index():
    return render_template('index.html', path=os.path.abspath(os.path.dirname(__file__)))

@app.route('/list')
def list():
    doms = conn.listAllDomains()
    out = []
    for dom in doms:
        out.append({ 'name' : dom.name(),
                     'state' : state_str(dom) })
    return jsonify({"domains" : out})

@app.route('/start')
def start_vm():
    name = request.args.get('name')
    if not name:
        return "404"
    return jsonify({ 'started' : name })
