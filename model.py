# -*- coding: utf-8 -*-
"""
时间: 2019/12/4 11:21

作者: nola2

更改记录:

重要说明:
"""

import datetime
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
        obj: posts

    """
    return db.select("blog_entries", order="id DESC")


def get_post(id):
    """获取一篇博客

    Args:
        id (int):  博客id

    Returns:
        obj: post

    """
    try:
        return db.select("blog_entries", where="id=$id", vars=locals())[0]
    except IndexError:
        return None


def new_post(title, text):
    """新增一篇博客

    Args:
        title (str): 博客标题
        text (str):  博客内容

    Returns:

    """
    db.insert(
        "blog_entries", title=title, content=text, posted_on=datetime.datetime.utcnow()
    )


def update_post(id, title, text):
    """更新一篇博客

    Args:
        id (int):  博客id
        title (str): 博客标题
        text (str):  博客内容

    Returns:

    """
    db.update("blog_entries", where="id=$id", vars=locals(), title=title, content=text)  # 使用id是区分内建id()，使用vars=locals()
