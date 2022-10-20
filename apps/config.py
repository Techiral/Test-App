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


#OPENAI_API_KEY=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