# -*- coding:utf-8 -*-
from mywebsite import db
from flask import Blueprint, render_template, session, current_app, request, flash, redirect, url_for, jsonify
from common import login_required
from mywebsite.models import Blog
admin_manage = Blueprint('admin', __name__)


@admin_manage.route('/')
@login_required
def admin():
    return 'haha'


@admin_manage.route('/login', methods=['GET'])
def login():
        return render_template('api_v1/login.html')


@admin_manage.route('/authentic', methods=['POST'])
def authentic():
    data_dict = request.form
    try:
        name = data_dict.get('name')
        password = data_dict.get('password')
    except Exception as e:
        current_app.logger.error(e)
        return
    if not all([name, password]):
        flash('参数不全')
        return redirect(url_for('login'))
    if name == '123' and password == '456':
        session['name'] = '123'
        session['password'] = '456'
    else:
        flash('账号或密码错误')
        return redirect(url_for('login'))
    return redirect(url_for('admin.add_blog'))


@admin_manage.route('/blog/add')
def add_blog():
    data_dict = request.json
    if not data_dict:
        print('没有数据')
        return render_template('api_v1/admin.html')
    title = data_dict.get('title')
    author = data_dict.get('author')
    desc = data_dict.get('desc')
    content = data_dict.get('content')
    if not all([title, author, desc, content]):
        print('参数不全')
        return jsonify(errno='1', errmsg='参数不全')
    blog = Blog()
    blog.name = title
    blog.author = author
    blog.desc = desc
    blog.content = content
    try:
        db.session.add(blog)
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        print('保存失败')
        return jsonify(errno='2', errmsg='保存失败')
    return jsonify(errno='0')