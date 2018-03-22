# -*- coding:utf8 -*-

import redis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session


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

    # Session扩展的配置
    # 将session保存到redis中
    # 如果没有设置SESSION_REDIS, 扩展会自动按照redis默认配置进行创建,
    SESSION_TYPE = "redis"
    # 手动创建
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 签名
    SESSION_USE_SIGNER = True
    # 过期时间: 单位 秒
    PERMANENT_SESSION_LIFETIME = 86400



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




@app.route("/index", methods=["GET", "POST"])
def index():
    session["usersession"] = "asession"
    redis_store.set("name", "one")
    return "index"

if __name__ == '__main__':
    app.run(host="0.0.0.0")