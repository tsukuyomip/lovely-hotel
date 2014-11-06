# coding: utf-8

import unittest
from main.client import Client


class TestClient(unittest.TestCase):
    def test_decide_equality_of_ids(self):
        client = Client(name="knskw")
        self.assertTrue(client.has_name("knskw"))
        self.assertFalse(client.has_name("knsk"))

    def test_decide_equality_of_email_addresses(self):
        client = Client(email="test@mail.com")
        self.assertTrue(client.has_email("test@mail.com"))
        self.assertFalse(client.has_email("false@test.com"))

    def test_decide_equality_of_passwords(self):
        client = Client(address="888-555")
        self.assertTrue(client.has_address("888-555"))
        self.assertFalse(client.has_address("88-555"))


if __name__ == "__main__":
    unittest.main()
