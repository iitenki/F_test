# -*- coding:utf8 -*-

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session

import logging
from logging.handlers import RotatingFileHandler
from config import config
from utils.common import RegexConverter



# 方法一: 先创建为None, 再在类中定义时设为全局变量
redis_store = None

# 方法二: 先初始化, 然后使用init方法加载app
db = SQLAlchemy()

csrf = CSRFProtect()



# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)






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

    #将自定义的转换器添加到路由视图映射中
    app.url_map.converters["re"] = RegexConverter


    # 在注册时导入, 否则会循环导入
    from web_pro.api_1_0 import api
    # 注册蓝图
    app.register_blueprint(api)

    # 注册访问静态文件蓝图
    from web_pro.web_html import w_html
    app.register_blueprint(w_html)

    return app