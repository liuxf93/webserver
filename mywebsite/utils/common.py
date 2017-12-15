# coding=utf-8
from flask import session, redirect, url_for
import functools


# 检测管理员登录的装饰器
def login_required(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        user = session.get('user')
        if not user:
           return redirect(url_for('admin.login'))
        return f(*args,**kwargs)
    return wrapper
