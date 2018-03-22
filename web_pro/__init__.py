# -*- coding:utf8 -*-

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session


from config import config


# 方法一: 先创建为None, 再在类中定义时设为全局变量
redis_store = None

# 方法二: 先初始化, 然后使用init方法加载app
db = SQLAlchemy()

csrf = CSRFProtect()

def create_app(config_name):
    """工厂方法:根据传入的内容,生成指定内容所对应的对象"""

    app = Flask(__name__)

    # 从对象中加载配置
    app.config.from_object(config[config_name])

    # 初始化mysql数据库
    # db = SQLAlchemy(app)
    # 关联当前app
    db.init_app(app)

    # 初始化redis数据库
    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)

    # 集成CSRF保护: 校验cookie中的CSRF和表单中提交过来的CSRF是否一样
    # csrf = CSRFProtect(app)
    csrf.init_app(app)

    # 集成session
    Session(app)