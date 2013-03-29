#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"David Kua"
SITENAME = u"A repository of my thoughts | David Kua"
SITEURL = "http://davidkua.com"

# My links
GITHUBURL = "http://github.com/dkua"
TWITTERURL = "http://twitter.com/davidkua"
EMAIL = "david@davidkua.com"

DEFAULT_LANG = u"en"
TIMEZONE = "UTC"
DEFAULT_DATE_FORMAT = ('%B %d, %Y')

DEFAULT_PAGINATION = 10

THEME = "theme/"

# Allows for blogging with IPython notebooks
PLUGINS = ["pelican.plugins.ipythonnb"]
MARKUP = ("md", "ipynb")

# Make sure CNAME is always ouputted
FILES_TO_COPY = (('CNAME', 'CNAME'),)

# Navigation links' pages
DIRECT_TEMPLATES = (("index", "about", "projects"))

USE_FOLDER_AS_CATEGORY = True

OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = (".ipynb")