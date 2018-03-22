# -*- coding:utf8 -*-

from flask import Flask

class Config(object):
    """项目配置"""
    DEBUG = True


app = Flask(__name__)

# 从对象中加载配置
app.config.from_object(Config)


@app.route("/index")
def index():
    return "index"

if __name__ == '__main__':
    app.run()