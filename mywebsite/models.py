# -*- coding:utf-8 -*-
#ihome所使用的所有模型

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""

    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


class User(BaseModel, db.Model):
    """用户"""

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    name = db.Column(db.String(32), unique=True, nullable=False)  # 用户昵称
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    avatar_url = db.Column(db.String(128))  # 用户头像路径

    @property  # 将方法提升为属性， 通过对象.xxxx去调用
    def password(self):
        raise AttributeError('该属性不能访问')

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        user_dict = {
            'user_id': self.id,
            'avatar_url': self.avatar_url,
            'name': self.name
        }
        return user_dict


class Blog(BaseModel, db.Model):
    """城区"""

    __tablename__ = "blog"

    id = db.Column(db.Integer, primary_key=True)  # 区域编号
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String(32), nullable=False)  # 区域名字
    author = db.Column(db.String(32))
    user = db.relationship('User', backref='blog')
    desc = db.Column(db.String(100))
    content = db.Column(db.Text())
    comment = db.Column(db.String(100))
    reply = db.Column(db.String(100))

