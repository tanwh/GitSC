#coding:utf-8

import unicodedata
import re

import json
from sqlalchemy.ext.declarative import DeclarativeMeta

# 检查登陆
def check_login(request):
    if request.remote_addr == request.server_addr:
        logged = session.get('logged_in', None)
        return logged

# json转码
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata' and x != 'query' and x != 'query_class']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data, ensure_ascii = False) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = str(data)
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

# 返回内容
def show_result_content(obj):
    return json.dumps(obj, cls=AlchemyEncoder,ensure_ascii = False) #json文本

# 返回成功提示
def show_result_success():
    return json.dumps({'result':'Success'})

# 返回失败提示
def show_result_fail():
    return json.dumps({'result':'Failed'})
