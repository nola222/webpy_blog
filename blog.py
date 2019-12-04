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
    "/", "Index",  # 首页
    "/new", "New",  # 新增页
    "/view/(\d+)", "View",  # 查看页
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


class New:
    """添加处理类

    """
    form = web.form.Form(
        web.form.Textbox("title", web.form.notnull, size=30, description="Post title:"),
        web.form.Textarea(
            "content", web.form.notnull, rows=30, cols=80, description="Post content:"
        ),
        web.form.Button("Post entry"),
    )

    def GET(self):
        """获取表单

        Returns:

        """
        form = self.form()  # 调用Form类__call__返回form
        return render.new(form)  # new --> new.html新增页

    def POST(self):
        """提交表单

        Returns:

        """
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.title, form.d.content)
        raise web.seeother("/")


class View:
    """查看博客类

    """
    def GET(self, id):
        """查看一篇博客

        Args:
            id (int): 博客id

        Returns:

        """
        post = model.get_post(id)
        return render.view(post)


app = web.application(urls, globals())  # 使用上面列出的url创建一个应用程序，在url对应命名空间查找该类

if __name__ == '__main__':
    app.run()
