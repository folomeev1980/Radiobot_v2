# -*- coding: utf-8 -*-
# flake8: noqa: F401
# noreorder
"""
Pytube: a very serious Python library for downloading YouTube Videos.
"""
__title__ = "pytube3"
__author__ = "Nick Ficano, Harold Martin"
__license__ = "MIT License"
__copyright__ = "Copyright 2019 Nick Ficano"

from pytube3.version import __version__
from pytube3.streams import Stream
from pytube3.captions import Caption
from pytube3.query import CaptionQuery
from pytube3.query import StreamQuery
from pytube3.__main__ import YouTube
from pytube3.contrib.playlist import Playlist
