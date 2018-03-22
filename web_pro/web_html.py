# -*- coding:utf8 -*-

from flask import Blueprint, current_app

# 创建静态文件访问的蓝图
w_html = Blueprint("whtml", __name__)


# 定义静态文件访问的路由
@w_html.route("/<file_name>")
def get_html_file(file_name):

    if file_name != "favicon.ico":

        file_name = "html/" + file_name

    # 通过当前app去查找到静态文件夹下的指定文件
    return current_app.send_static_file(file_name)
