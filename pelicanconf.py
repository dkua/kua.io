#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'David Kua'
AUTHOR_EMAIL = 'david@davidkua.com'
SITENAME = u'David Kua'
SITEURL = ''
TAGLINE = "Code and carrot cake"

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
    ("Posts", "/posts"),
)

GITHUB_URL = "https://github.com/dkua"
TWITTER_USERNAME = "davidkua"
SOCIAL = (
    ("github", GITHUB_URL),
    ("twitter", "http://twitter.com/" + TWITTER_USERNAME),
)

DEFAULT_PAGINATION = 10

PROFILE_IMG_URL = "/images/dkua_icon.png"
COVER_IMG_URL = "/images/cover.jpg"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DATE_FORMATS = {
    'en': '%B %d, %Y',
}
ARTICLE_URL = 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'
ARCHIVES_SAVE_AS = "posts/index.html"
YEAR_ARCHIVE_SAVE_AS = "posts/{date:%Y}/index.html"

PAGE_URL = "{slug}/index.html"
PAGE_SAVE_AS = "{slug}/index.html"
