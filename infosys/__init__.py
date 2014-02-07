from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession
from .models.base import  Base

from pyramid.renderers import JSONP

engine = None

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    # jsonp crud
    config.add_route('jsonp_crud_model', '/crud/jsonp/{model}')
    config.add_route('jsonp_crud_model:command', '/crud/jsonp/{model}/{command}')
    config.add_renderer('jsonp', JSONP(param_name='callback'))
    # json crud
    config.add_route('json_crud_model', '/crud/json/{model}')
    config.add_route('json_crud_model:command', '/crud/json/{model}/{command}')
    config.scan()
    return config.make_wsgi_app()
