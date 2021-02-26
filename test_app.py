#!/usr/bin/env python
import unittest
import app
from app import hello


class TestApp(unittest.TestCase):
  def setUp(self):
    app.app.testing=True
    self.app = app.app.test_client()

  def test_hello(self):
    self.assertTrue(hello() == "Hello KPN!")

  def test_hello_serv(self):
    rv = self.app.get('/')
    self.assertEqual(rv.status, '200 OK')
    self.assertEqual(rv.data, b'Hello KPN!')

if __name__ == '__main__':
  import xmlrunner
  runner = xmlrunner.XMLTestRunner(output='reports')
  unittest.main(testRunner=runner)
