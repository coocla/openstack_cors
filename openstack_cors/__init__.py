# -*- coding:utf-8 -*-
import webob.exc

class CorsMixin(HttpProtocol):
    def __init__(self, application):
        self.application = application

    @classmethod
    def factory(cls, global_config, **local_config):
        def _factory(app):
            return cls(app, **local_config)
        return _factory

    def __call__(self, environ, start_response):
        if environ['REQUEST_METHOD'] == 'OPTIONS':
            return self._OPTIONS(environ, start_response)

        def custom_start_response(status, headers, exc_info=None):
            headers.append(('Access-Control-Allow-Origin', '*'))
            headers.append(('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH'))
            headers.append(('Access-Control-Allow-Headers', 'X-Auth-Token, Content-Type'))
            return start_response(status, headers, exc_info)
    
        return self.application(environ, custom_start_response)

    def _OPTIONS(self, environ, start_response):
        headers = [('Access-Control-Allow-Origin', '*'),
                   ('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH'),
                   ('Access-Control-Allow-Headers', 'X-Auth-Token, Content-Type')]
        resp = webob.exc.HTTPAccepted('Options Accept', headers)
        return resp(environ, start_response)
