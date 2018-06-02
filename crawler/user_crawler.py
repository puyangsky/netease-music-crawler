#!/usr/bin/env python
# encoding: utf-8

"""
@author: puyangsky
@file: user_crawler.py
@time: 2018/6/2 上午1:24
"""

import requests
import json
from model import *
from base import *
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOG = logging.getLogger("user_crawler")
MAX_RETRY_TIMES = 3


def __validate_param(*params):
    result = True
    for param in params:
        result &= param is not None and param != ""
    return result


def search(key, search_type):
    if not __validate_param(key, search_type):
        LOG.error("bad parameter")
        return None
    data = {
        "s": key,
        "type": search_type
    }
    i = 0
    resp = None
    while i < MAX_RETRY_TIMES:
        i += 1
        resp = requests.post(url=SEARCH_URL, headers=HEADERS, data=data)
        if resp.status_code != 200:
            LOG.error("%d th request to %s failed" % (i, SEARCH_URL))
            continue
        else:
            break
    return resp


def fetch_user_list(username):
    user_list = list()
    resp = search(username, SEARCH_USER_TYPE)
    if resp is not None and resp.content is not None:
        js = json.loads(resp.content)
        if "result" in js:
            result = js["result"]
            if "userprofiles" in result:
                userprofiles = result["userprofiles"]
                for userprofile in userprofiles:
                    uid = userprofile["userId"]
                    username = userprofile["nickname"]
                    avatar = userprofile["avatarUrl"]
                    gender = userprofile["gender"]
                    user = User(uid, username, avatar, gender)
                    user_list.append(user)
    LOG.info("fetch %d users with search: %s" % (len(user_list), username))
    return user_list


if __name__ == '__main__':
    fetch_user_list("puyangsky")
