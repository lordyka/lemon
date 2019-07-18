#!/usr/bin/env python3
# coding=utf8

import os
import falcon

from ledhat import LedHat
from clock import Clock
from middleware_json import MiddlewareJson

from resource_api import ResourceApi

class Lemon:
    def __init__(self):

        self._ledhat = LedHat()
        self._clock = Clock()
        
        self._ledhat.icon('lemon')

        self._app = falcon.API(middleware=[
            MiddlewareJson(),
        ])

        self._ledhat.text('Lemon')
        self._clock()
        self._api = ResourceApi(ledhat=self._ledhat, clock=self._clock)

        self._app.add_route('/api', self._api)
        
lemon = Lemon()
app = lemon._app
