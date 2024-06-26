import requests
import copy

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

from .auth_handler import AuthHandler
from .error_handler import ErrorHandler
from .request_handler import RequestHandler
from .response import Response
from .response_handler import ResponseHandler


class HttpClient(object):

    """Main HttpClient which is used by API classes"""

    def __init__(self, auth, options):

        if isinstance(auth, str):
            auth = {'http_header': auth}

        self.options = {
            'base': 'https://api.quickemailverification.com',
            'api_version': 'v1',
            'user_agent': 'quickemailverification-python/1.0.4 (https://github.com/quickemailverification/quickemailverification-python)'
        }

        self.options.update(options)

        self.base = self.options['base']

        self.headers = {
            'user-agent': self.options['user_agent']
        }

        if 'headers' in self.options:
            self.headers.update(self.dict_key_lower(self.options['headers']))
            del self.options['headers']

        self.auth = AuthHandler(auth)

    def get(self, path, params={}, options={}):
        options.update({'query': params})
        return self.request(path, None, 'get', options)

    def post(self, path, body={}, options={}):
        return self.request(path, body, 'post', options)

    def patch(self, path, body={}, options={}):
        return self.request(path, body, 'patch', options)

    def delete(self, path, body={}, options={}):
        return self.request(path, body, 'delete', options)

    def put(self, path, body={}, options={}):
        return self.request(path, body, 'put', options)

    def request(self, path, body, method, options):
        """Intermediate function which does three main things

        - Transforms the body of request into correct format
        - Creates the requests with given parameters
        - Returns response body after parsing it into correct format
        """
        kwargs = copy.deepcopy(self.options)
        kwargs.update(options)

        kwargs['headers'] = copy.deepcopy(self.headers)

        if 'headers' in options:
            kwargs['headers'].update(self.dict_key_lower(options['headers']))

        kwargs['data'] = body
        kwargs['allow_redirects'] = True

        kwargs['params'] = kwargs['query'] if 'query' in kwargs else {}

        if 'query' in kwargs:
            del kwargs['query']

        if 'body' in kwargs:
            del kwargs['body']

        del kwargs['base']
        del kwargs['user_agent']

        if method != 'get':
            kwargs = self.set_body(kwargs)

        kwargs['hooks'] = dict(response=ErrorHandler.check_error)

        kwargs = self.auth.set(kwargs)

        response = self.create_request(method, path, kwargs)

        return Response(
            self.get_body(response), response.status_code, response.headers
        )

    def create_request(self, method, path, options):
        """Creating a request with the given arguments

        If api_version is set, appends it immediately after host
        """
        version = '/' + options['api_version'] if 'api_version' in options else ''

        path = urlparse.urljoin(self.base, version + path)

        if 'api_version' in options:
            del options['api_version']

        if 'response_type' in options:
            del options['response_type']

        return requests.request(method, path, **options)

    def get_body(self, response):
        """Get response body in correct format"""
        return ResponseHandler.get_body(response)

    def set_body(self, request):
        """Set request body in correct format"""
        return RequestHandler.set_body(request)

    def dict_key_lower(self, dic):
        """Make dict keys all lower case"""
        return dict(zip(map(self.key_lower, dic.keys()), dic.values()))

    def key_lower(self, key):
        """Make a function for lower case"""
        return key.lower()
