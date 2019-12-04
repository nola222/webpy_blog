# -*- coding: utf-8 -*-
"""blog
时间: 2019/12/2 15:46

作者: nola2

更改记录:

重要说明:
"""

import model
import web

# Urls Configuration
urls = (
    "/",
    "Index",  # 首页
)

# Templates
t_gloabls = {"datestr": web.datestr}  # 设置全局变量 可通过键获取datestr对象
render = web.template.render("templates", base="base", globals=t_gloabls)  # base-->基模板


class Index:
    """首页处理类

    """
    def GET(self):  # GET必须大写
        """显示首页，博客列表

        Returns:

        """
        posts = model.get_posts()
        return render.index(posts)  # index为首页index.html名称


app = web.application(urls, globals())  # 使用上面列出的url创建一个应用程序，在url对应命名空间查找该类

if __name__ == '__main__':
    app.run()
