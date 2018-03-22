# -*- coding:utf8 -*-

import redis

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


class DevelopementConfig(Config):
    """开发阶段配置"""
    # 开启调试模式
    DEBUG = True


class ProductionConfig(Config):
    """生产环境下所需的配置"""
    pass


config = {
    "developement": DevelopementConfig,
    "production": ProductionConfig
}