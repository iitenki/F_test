# -*- coding:utf8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    """项目配置"""

    DEBUG = True


    # 数据库链接配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/F_test1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)

# 从对象中加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)




@app.route("/index")
def index():
    return "index"

if __name__ == '__main__':
    app.run()