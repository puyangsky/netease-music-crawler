#!/usr/bin/env python
# encoding: utf-8

"""
@author: puyangsky
@file: model.py
@time: 2018/6/2 下午6:43
"""


class User(object):
    def __init__(self, uid, username, avatar, gender):
        self.uid = uid
        self.username = username
        self.avatar = avatar
        self.gender = gender
