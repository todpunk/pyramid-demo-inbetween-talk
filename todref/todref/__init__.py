# -*- coding: utf-8 -*-
import datetime

from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(
        settings=settings,
    )
    config.include('cornice')
    config.include('todref.models')

    config.add_route('api', '/api')

    config.scan()
    return config.make_wsgi_app()
