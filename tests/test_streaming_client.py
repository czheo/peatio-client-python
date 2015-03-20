# coding:utf-8
import unittest2
from peatio_client import StreamingClient, ClientError

class StreamingClientTestCase(unittest2.TestCase):
    def test_init(self):
        sc = StreamingClient(
            access_key= "access",
            secret_key = "secret"
        )

        self.assertEqual("access", sc.access_key)
        self.assertEqual("secret", sc.secret_key)
