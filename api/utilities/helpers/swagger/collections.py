""" Module for swagger collections """

from config.server import api

# Remove default namespace
api.namespaces.clear()

user_namespace = api.namespace(
    'Users',
    description='A Collection of User related endpoints',
    path='/auth'
)
