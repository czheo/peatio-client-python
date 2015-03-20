# coding: utf-8
from .auth import Auth
from .error import ClientError
import logging
import websocket
import json

class StreamingClient:
    def __init__(self,
        access_key,
        secret_key,
        endpoint = "wss://yunbi.com:8080",
        logger = None 
    ):
        self.endpoint = endpoint
        self.access_key = access_key
        self.secret_key = secret_key
        self.auth = Auth(access_key, secret_key)
        if logger is None:
            logger = logging.getLogger(__name__)
            # initialize the logger
            handler = logging.StreamHandler()
            handler.setLevel(logging.INFO)
            logger.setLevel(logging.INFO)
            logger.addHandler(handler)
        self.logger = logger

    
    def run(self, on_message=None):
        if on_message is not None:
            self.on_message = on_message

        def on_open(ws):
            self.logger.info("Connected!")

        def on_message(ws, message):
            msg = json.loads(message)
            if "challenge" in msg:
                data = msg["challenge"]
                ws.send(json.dumps(self.auth.signed_challenge(data)))
            else:
                try:
                    self.on_message(msg)
                except Exception as e:
                    self.logger.error(e)
                    self.logger.error("Failed to process message: %s" % message)

        def on_close(ws):
            self.logger.info("Closed!")

        def on_error(ws, error):
            self.logger.error(error)
            raise ClientError(error)

        ws = websocket.WebSocketApp(self.endpoint)
        ws.on_open = on_open
        ws.on_message = on_message
        ws.on_close = on_close
        ws.on_error = on_error
        ws.run_forever()
