# -*- coding: utf-8 -*-
"""
时间: 2019/12/4 11:21

作者: nola2

更改记录:

重要说明:
"""

import web

import config

# 实例化db
db = web.database(dbn=config.DBN,
                  host=config.HOST,
                  port=config.PORT,
                  user=config.USER,
                  pw=config.PW,
                  db=config.DB)


def get_posts():
    """获取所有博客

    Returns:

    """
    return db.select("entries", order="id DESC")
