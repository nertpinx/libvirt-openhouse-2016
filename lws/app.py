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
    return render_template('index.html')

@app.route('/list')
def list():
    doms = conn.listAllDomains()
    out = {}
    for dom in doms:
        out[dom.name()] = { 'info' : { 'status' : state_str(dom) }}
    return jsonify({"domains" : out})

@app.route('/do/<action>')
def doAction(action):
    name = request.args.get('name')
    ret = {};

    if not name:
        return jsonify({ 'error' : 'Missing argument "name"' });

    try:
        dom = conn.lookupByName(name)
        attr = getattr(dom, action, None);

        if not attr:
            ret = { 'error' : 'Unsupported action "%s"' % action }
        elif action == 'interfaceAddresses':
            for inet, data in attr(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_LEASE).items():
                ret = { 'update' : { name : { 'info' : { 'address' : data['addrs'][0]['addr']}}}}
                break
            if not ret:
                ret = { 'error' : 'No address found for domain "%s"' % name }
        else:
            attr()
            ret = { 'update' : { name : { 'info' : {'status' : state_str(dom) }}}}
    except (libvirt.libvirtError) as e:
        ret = { 'error' : str(e) }

    return jsonify(ret)
