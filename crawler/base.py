#!/usr/bin/env python
# encoding: utf-8

"""
@author: puyangsky
@file: base.py
@time: 2018/6/2 上午1:18
"""


"""
API 参考 http://moonlib.com/606.html
"""

SEARCH_URL = "http://music.163.com/api/search/pc"
HEADERS = {
    "Host": "music.163.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "http://music.163.com/",
    "Cookie": "appver=1.5.0.75771;",
}

SEARCH_SONG_TYPE = 1
SEARCH_ALBUM_TYPE = 10
SEARCH_SINGER_TYPE = 100
SEARCH_SONG_LIST_TYPE = 1000
SEARCH_USER_TYPE = 1002
SEARCH_MV_TYPE = 1004
SEARCH_LYRIC_TYPE = 1006
SEARCH_RADIO_TYPE = 1009

