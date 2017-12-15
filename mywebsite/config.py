# -*- coding:utf-8 -*-
import redis


class Config(object):
    SECRET_KEY = 'aiUGgAK4dVCe4m4jyo6czOQij8w4joYs'
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:lxf@127.0.0.1:3306/iblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMNENT_SESSION_LIFETIME = 86400


class DevelopmentConfig(Config):
    '''开发者模式的配置'''
    DEBUG = True


class ProductionConfig(Config):
    '''生产环境下的配置（上线的环境）'''
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}