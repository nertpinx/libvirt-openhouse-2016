#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import flask
from flask.ext.script import Manager, Command

from lws.app import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
