#!/usr/bin/env python
import unittest
from app import app


class TestApp(unittest.TestCase):
  
  def setUp(self):
    app.app.Testing=True
    self.app=app.app.test_client()
    
  def test_hello(self):
    rv=self.app.get('/')
    self.assertEqual(rv.data, b'Hello World')
 
if __name__ == '__main__':
  unittest.main()
