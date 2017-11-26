#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andrew Lane'
SITENAME = u'Andrew Lane'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/alanescience'),
                    ('github', 'https://github.com/alanecode'),
                    ('envelope','mailto:science@ajlane.me'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# static files
STATIC_PATHS = [
    'images',
    'slides',
    'slides/css/theme',
    'slides/lib/css',
    'slides/lib/js',
    'slides/js',
    'slides/plugin/markdown',
    'slides/plugin/highlight',
    'slides/plugin/notes',
    ]

EXTRA_PATH_METADATA = {
    'slides/css/theme/night.css': {'path': 'slides/css/theme/night.css'},

    'slides/js/reveal.js': {'path': 'slides/js/reveal.js'},
    
    'slides/lib/css/zenburn.css': {'path': 'slides/lib/css/zenburn.css'},
    'slides/lib/js/head.min.js': {'path': 'slides/lib/js/head.min.js'},
    'slides/lib/js/classList.js': {'path': 'slides/lib/js/classList.js'},

    'slides/plugin/markdown/marked.js': {'path':
    'slides/plugin/markdown/marked.js'},
    

    'slides/plugin/markdown/markdown.js': {'path':
    'slides/plugin/markdown/markdown.js'},

    'slides/plugin/highlight/highlight.js': {'path':
    'slides/plugin/highlight/highlight.js'},

    'slides/plugin/notes/notes.js': {'path':
    'slides/plugin/notes/notes.js'},

    'slides/plugin/math/math.js' : {'path': 'slides/plugin/math/math.js'},

    'slides/earth-modelling.html': {'path': 'slides/earth-modelling.html'},

    'slides/learning-from-models.html': {'path': 'slides/learning-from-models.html'}

    }

READERS = {"html": None}

ARTICLE_EXCLUDES = [
    'slides/earth-modelling.html',
    'slides/learning-from-models.html'

    ]


# colour scheme for code highlights
COLOR_SCHEME_CSS = 'tomorrow.css'

# header colour
HEADER_COLOR = '#07162B'
    
