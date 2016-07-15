""" Cornice services.
"""
from cornice import Service
from todref.models.mymodel import MyModel


hello = Service(name='hello', path='/api/hello', description="Simplest app")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

mymodels_svc = Service(name='mymodels', path='/api/mymodels', description="Working with models")

@mymodels_svc.get()
def mymodels_get_view(request):
    """ Return all models in the db"""
    results = request.dbsession.query(MyModel).all()
    return {'d': [{'id': int(x.id),
                   'name': x.name,
                   'value': x.value
                   } for x in results]}
    