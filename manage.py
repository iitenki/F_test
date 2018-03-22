# -*- coding:utf8 -*-

import redis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from config import Config

app = Flask(__name__)

# 从对象中加载配置
app.config.from_object(Config)

# 初始化mysql数据库
db = SQLAlchemy(app)

# 初始化redis数据库
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 集成CSRF保护: 校验cookie中的CSRF和表单中提交过来的CSRF是否一样
csrf = CSRFProtect(app)

# 集成session
Session(app)

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