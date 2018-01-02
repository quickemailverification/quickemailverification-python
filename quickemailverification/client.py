from .http_client import HttpClient

# Assign all the api classes
from .api.quickemailverification import Quickemailverification


class Client(object):

    def __init__(self, auth={}, options={}):
        self.http_client = HttpClient(auth, options)

    def quickemailverification(self):
        """QuickEmailVerification Class for email verification
        """
        return Quickemailverification(self.http_client)

