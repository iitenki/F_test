# -*- coding:utf8 -*-

import redis
from flask import session

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from config import Config
from web_pro import create_app, db, redis_store


app = create_app("developement")
# 使用命令行运行
manager = Manager(app)
# 集成数据库迁移
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@app.route("/index", methods=["GET", "POST"])
def index():
    session["usersession"] = "asession"
    redis_store.set("name", "one")
    return "index"

if __name__ == '__main__':
    # app.run(host="0.0.0.0")
    manager.run()