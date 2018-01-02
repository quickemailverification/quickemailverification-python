import six

class Quickemailverification(object):

    """QuickEmailVerification Class for email verification
    """

    def __init__(self, client):
        self.client = client

    def verify(self, email, options={}):
        """Verify email address and get detailed response

        '/verify?email=:email' GET

        Args:
            email: send email address in query parameter
        """
        body = options['query'] if 'query' in options else {}

        email   = six.moves.urllib.parse.quote(email)
        response = self.client.get('/verify?email=' + email + '', body, options)

        return response

