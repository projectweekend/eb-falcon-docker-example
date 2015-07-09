import os
import json
import falcon


class HelloResource(object):

    def on_get(self, req, res):

        res.status = falcon.HTTP_200
        res.body = json.dumps({
            'message': "hello!"
        })


class TestVariableResource(object):

    def on_get(self, req, res):

        res.status = falcon.HTTP_200
        res.body = json.dumps({
            'message': os.getenv('TEST_THING')
        })
