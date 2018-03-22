# -*- coding:utf8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis

class Config(object):
    """项目配置"""

    DEBUG = True


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



@app.route("/index")
def index():
    redis_store.set("name", "one")
    return "index"

if __name__ == '__main__':
    app.run()