# coding=utf-8
"""
wecube_plugins_itsdangerous.server.wsgi_server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

本模块提供wsgi启动能力

"""

from __future__ import absolute_import

import base64
import os
import json
from talos.server import base
from talos.core import utils
from wecube_plugins_itsdangerous.server import conf_intercepter
from talos.core import config


@config.intercept('itsdangerous_db_username', 'itsdangerous_db_password', 'itsdangerous_db_hostip',
                  'itsdangerous_db_hostport', 'itsdangerous_db_schema', 'gateway_url', 'jwt_signing_key')
def get_env_value(value, origin_value):
    prefix = 'ENV@'
    if value.startswith(prefix):
        env_name = value[len(prefix):]
        return os.getenv(env_name, default='')
    raise ValueError('config intercepter of get_env_value support "ENV@" only')


def error_serializer(req, resp, exception):
    representation = exception.to_dict()
    representation['status'] = 'ERROR'
    representation['data'] = None
    resp.body = json.dumps(representation, cls=utils.ComplexEncoder)
    resp.content_type = 'application/json'


application = base.initialize_server('wecube_plugins_itsdangerous',
                                     os.environ.get('WECUBE_PLUGINS_ITSDANGEROUS_CONF',
                                                    './etc/wecube_plugins_itsdangerous.conf'),
                                     conf_dir=os.environ.get('WECUBE_PLUGINS_ITSDANGEROUS_CONF_DIR',
                                                             './etc/wecube_plugins_itsdangerous.conf.d'))
application.set_error_serializer(error_serializer)