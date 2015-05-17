import json
import falcon


class HelloResource(object):

    def on_get(self, req, res):

        res.status = falcon.HTTP_200
        res.body = json.dumps({
            'message': "hello!"
        })
