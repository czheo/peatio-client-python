# coding: utf-8
import hashlib, hmac
import urllib
import time

def payload(verb, path, params):
    # url params should to sorted in alphabet
    url_params = urllib.urlencode(sorted(params.items()))
    return "{verb}|{path}|{url_params}".format(
        verb = verb.upper(),
        path = path,
        url_params = url_params
    )

class Auth:
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key

    def signed_params(self, verb, path, params):
        params = params.copy()
        params = self._format_params(params)
        signature = self.sign(verb, path, params)
        params["signature"] = signature
        return params

    def sign(self, verb, path, params):
        return hmac.new(self.secret_key, payload(verb, path, params), hashlib.sha256).hexdigest() 

    def _format_params(self, params):
        if not params.get("access_key"):
            params["access_key"] = self.access_key
        if not params.get("tonce"):
            params["tonce"] = int(time.time() * 1000)
        return params
