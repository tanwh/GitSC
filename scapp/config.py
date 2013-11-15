#coding:utf-8

import os

_HERE = os.path.dirname(__file__)
_DB_SQLITE_PATH = os.path.join(_HERE, 'scapp.sqlite')

_DBUSER = "root"  # 数据库用户名
_DBPASS = "root"  # 数据库用户名密码
_DBHOST = "192.168.0.250"  # 服务器
_DBNAME = "sc_schema"  # 数据库名称

PER_PAGE = 20  # 每页数量
UPLOAD_FOLDER_REL = '/static/upload/' #上传目录(相对路径)
UPLOAD_FOLDER_ABS = os.path.join(_HERE,'static\\upload') #上传目录(绝对路径)

class Config(object):
    SECRET_KEY = '\xb5\xc8\xfb\x18\xba\xc7*\x03\xbe\x91{\xfd\xe0L\x9f\xe3\\\xb3\xb1P\xac\xab\x061'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % _DB_SQLITE_PATH
    BABEL_DEFAULT_TIMEZONE = 'Asia/Chongqing'


class ProConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s' % (_DBUSER, _DBPASS, _DBHOST, _DBNAME)
    DEBUG = True

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True

    
