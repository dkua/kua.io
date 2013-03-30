#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"David Kua"
SITENAME = u"A repository for my thoughts | David Kua"
SITEURL = "http://davidkua.com"

# My links
GITHUBURL = "http://github.com/dkua"
TWITTERURL = "http://twitter.com/davidkua"
EMAIL = "david@davidkua.com"

DEFAULT_LANG = u"en"
TIMEZONE = "UTC"
DEFAULT_DATE_FORMAT = ('%B %d, %Y')

# Changes the output URL and file locations
ARTICLE_URL = "notes/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "notes/{date:%Y}/{date:%m}/{slug}/index.html"

DEFAULT_PAGINATION = 10

THEME = "theme/"

# Allows for blogging with IPython notebooks
PLUGINS = ["pelican.plugins.ipythonnb"]
MARKUP = ("md", "ipynb")

# Make sure CNAME is always ouputted
FILES_TO_COPY = (('CNAME', 'CNAME'),)

# Navigation links' pages
DIRECT_TEMPLATES = (("index", "about", "projects"))

# Use souce folder as the category
USE_FOLDER_AS_CATEGORY = True

# Copy images and IPython Notebooks to the static folder
STATIC_PATHS = (["images", "2013"])