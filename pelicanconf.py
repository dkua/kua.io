#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'David Kua'
AUTHOR_EMAIL = 'david@davidkua.com'
SITENAME = u'David Kua'
SITEURL = ''
TAGLINE = "Code, cookies, and more"

THEME = "../pure-single"

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Menu
MENUITEMS = (
    ("Home", "/"),
    ("About", "/about"),
    ("Archive", "/archive"),
)

SOCIAL = (
    ("github", "https://github.com/dkua"),
    ("twitter", "https://twitter.com/davidkua"),
)

DEFAULT_PAGINATION = 10

PROFILE_IMG_URL = "images/dkua_icon.png"
COVER_IMG_URL = "images/cover.jpg"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
