# -*- coding:utf8 -*-

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


class Config(object):
    """项目配置"""

    DEBUG = True


    SECRET_KEY = "FCdTmFCgyDcIFwpu3KEUpivlp20ZBmG+PTK0wKjrvJxFwsD6TUJmUiRc+0dnS5xL"

    # mysql数据库链接配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/F_test1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # redis数据库配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379



app = Flask(__name__)

# 从对象中加载配置
app.config.from_object(Config)

# 初始化mysql数据库
db = SQLAlchemy(app)

# 初始化redis数据库
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 集成CSRF保护: 校验cookie中的CSRF和表单中提交过来的CSRF是否一样
csrf = CSRFProtect(app)




@app.route("/index", methods=["GET", "POST"])
def index():
    redis_store.set("name", "one")
    return "index"

if __name__ == '__main__':
    app.run(host="0.0.0.0")