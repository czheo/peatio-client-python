# coding:utf-8
import unittest2
from peatio_client import Client, ClientError

class ClientTestCase(unittest2.TestCase):
    def test_access_private_apis_without_keys(self):
        with self.assertRaises(ClientError):
            client = Client().post("")

    def test_init_with_options(self):
        c = Client(access_key="access", secret_key="secret")
        self.assertEqual("access", c.access_key)
        self.assertEqual("secret", c.secret_key)
