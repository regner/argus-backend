#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_restful import Resource


class Liveness(Resource):
    def get(self):
        return {}, 200
