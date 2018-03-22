# -*- coding:utf8 -*-

from . import api
from flask import session
from web_pro import redis_store

@api.route("/index", methods=["GET", "POST"])
def index():
    session["usersession"] = "asession"
    redis_store.set("name", "one")
    return "index"