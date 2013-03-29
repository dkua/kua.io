#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"David Kua"
SITENAME = u"A repository of my thoughts | David Kua"
SITEURL = "http://davidkua.com"

DEFAULT_LANG = u"en"
TIMEZONE = "UTC"
DEFAULT_DATE_FORMAT = ('%B %d, %Y')

DEFAULT_PAGINATION = 10

THEME = "theme/"

# Allows for blogging with IPython notebooks
PLUGINS = ["pelican.plugins.ipythonnb"]
MARKUP = ("md", "ipynb")

# Default files to always output
FILES_TO_COPY = (('default/CNAME', 'CNAME'),)

DIRECT_TEMPLATES = (("index", "about", "projects"))