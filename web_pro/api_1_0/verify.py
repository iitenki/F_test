# -*- coding:utf8 -*-

# 验证码: 图片验证码, 短信验证码

from . import api
from flask import request, abort, current_app, jsonify, make_response

from web_pro.utils.captcha.captcha import captcha
from web_pro import redis_store
from web_pro.constants import IMAGE_CODE_REDIS_EXPIRES
from web_pro.utils.response_code import RET


@api.route("/imagecode")
def get_image_code():
    """
    1. 取到图片编码
    2. 生成图片验证码
    3. 保存到redis中(key是图片编码, 值时验证码的文字内容)
    4. 返回验证码图片
    :return:
    """

    args = request.args
    cur = args.get("cur")

    # 如果用户没有传图片id, 直接抛错
    if not cur:
        abort(403)


    # 生成图片验证码
    # name, text, image = captcha.generate_captcha()

    # 不使用的参数可以用_
    _, text, image = captcha.generate_captcha()

    # 为了方便测试将验证码输出到控制台
    current_app.logger.debug(text)

    # 保存
    # redis_store.set("key", "value", "过期时间")
    try:
        redis_store.set("ImageCode_" + cur, text, IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存图片验证码失败")

    # 返回验证码图片
    response = make_response(image)
    return response