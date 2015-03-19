# coding: utf-8
import requests
from .auth import Auth
from .error import ClientError

class Client:
    def __init__(
        self,
        endpoint = "https://yunbi.com",
        access_key = None,
        secret_key = None,
        timeout = 60
    ):
        self.endpoint = endpoint
        self.timeout = timeout

        if access_key and secret_key:
            self.access_key = access_key
            self.secret_key = secret_key
            self.auth = Auth(access_key, secret_key)
        else:
            self.auth = False

    def check_auth(self):
        if not self.auth:
            raise ClientError("Missing access key and/or secret key")

    def get_public(self, path, params=None):
        if params is None:
            params = {}
        url = "%s%s" % (self.endpoint, path)

        response = requests.get(url,
            params = params,
            timeout = self.timeout,
            verify = self.endpoint.startswith("https://")
        )

        return self.response_to_dict(response)

    def get(self, path, params=None):
        if params is None:
            params = {}
        self.check_auth()
        url = "%s%s" % (self.endpoint, path)
        params = self.auth.signed_params("get", path, params)

        response = requests.get(url,
            params = params,
            timeout = self.timeout,
            verify = self.endpoint.startswith("https://")
        )

        return self.response_to_dict(response)

        
    def post(self, path, params=None):
        if params is None:
            params = {}
        self.check_auth()
        url = "%s%s" % (self.endpoint, path)
        params = self.auth.signed_params("post", path, params)
        
        response = requests.post(url,
            data = params,
            timeout = self.timeout,
            verify = self.endpoint.startswith("https://")
        )

        return self.response_to_dict(response)

    def response_to_dict(self, response):
        try:
            return response.json()
        except ValueError:
            raise ClientError("Response is in bad json format")
