from flask import render_template, current_app, jsonify
from . import api
from mywebsite.models import User, Blog


@api.route('/index')
def index():
    data_list = []
    try:
        blog_list = Blog.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno='-1')
    for blog in blog_list:
        data = dict()
        data['author'] = blog.user.name
        data['title'] = blog.name
        data['date'] = blog.update_time
        data['content'] = blog.content
        data['index'] = blog.id
        data_list.append(data)

    return render_template('api_v1/index.html', errno='0', data_list=data_list)