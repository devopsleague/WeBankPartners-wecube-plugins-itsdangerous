# coding=utf-8

from __future__ import absolute_import

from wecube_plugins_itsdangerous.apps.processor import controller


def add_routes(api):
    # policy
    api.add_route('/itsdangerous/ui/v1/policies', controller.CollectionPolicy())
    api.add_route('/itsdangerous/ui/v1/policies/{rid}', controller.ItemPolicy())
    # rule
    api.add_route('/itsdangerous/ui/v1/rules', controller.CollectionRule())
    api.add_route('/itsdangerous/ui/v1/rules/{rid}', controller.ItemRule())
    # matchparam
    api.add_route('/itsdangerous/ui/v1/matchparams', controller.CollectionMatchParam())
    api.add_route('/itsdangerous/ui/v1/matchparams/{rid}', controller.ItemMatchParam())
    # subject
    api.add_route('/itsdangerous/ui/v1/subjects', controller.CollectionSubject())
    api.add_route('/itsdangerous/ui/v1/subjects/{rid}', controller.ItemSubject())
    # target
    api.add_route('/itsdangerous/ui/v1/targets', controller.CollectionTarget())
    api.add_route('/itsdangerous/ui/v1/targets/{rid}', controller.ItemTarget())
    # box
    api.add_route('/itsdangerous/ui/v1/boxes', controller.CollectionBox())
    api.add_route('/itsdangerous/ui/v1/boxes/{rid}', controller.ItemBox())
