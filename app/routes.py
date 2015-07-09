from app import api
from hello import handlers as hello_handlers


api.add_route('/', hello_handlers.HelloResource())
api.add_route('/test', hello_handlers.HelloResource())
api.add_route('/whatever', hello_handlers.TestVariableResource())
