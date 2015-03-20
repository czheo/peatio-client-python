# coding: utf-8
import hashlib, hmac
try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode
import time

def payload(verb, path, params):
    # url params should be sorted in alphabet
    url_params = urlencode(sorted(params.items()))
    return "{verb}|{path}|{url_params}".format(
        verb = verb.upper(),
        path = path,
        url_params = url_params
    )

class Auth:
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key

    def signed_challenge(self, challenge):
        payload = "%s%s" % (self.access_key, challenge)
        signature = hmac.new(self.secret_key.encode(), payload.encode(), hashlib.sha256).hexdigest()
        return {
            "auth": {
                "access_key": self.access_key,
                "answer": signature
            }
        }

    def signed_params(self, verb, path, params):
        params = params.copy()
        params = self._format_params(params)
        signature = self.sign(verb, path, params)
        params["signature"] = signature
        return params

    def sign(self, verb, path, params):
        return hmac.new(self.secret_key.encode(), payload(verb, path, params).encode(), hashlib.sha256).hexdigest() 

    def _format_params(self, params):
        if not params.get("access_key"):
            params["access_key"] = self.access_key
        if not params.get("tonce"):
            params["tonce"] = int(time.time() * 1000)
        return params
