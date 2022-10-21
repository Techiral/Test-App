# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False   
    OPENAI_API_KEY= os.getenv('OPENAI_API_KEY', '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')
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
    FLASK_APP= "app"
    FLASK_ENV= "development"

