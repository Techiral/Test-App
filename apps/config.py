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

