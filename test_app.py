#!/usr/bin/env python
import unittest
import app

class TestApp(unittest.TestCase):
  def setUp(self):
    app.app.testing=True
    self.app = app.app.test_client()
  
  def test_hello(self):
    self.assertTrue(hello() == "Hello World!")
    
  def test_hello_serv(self):
    rv = self.app.get('/')
    self.assertEqual(rv.status, '200 OK')
    self.assertEqual(rv.data, b'Hello World!')
 
if __name__ == '__main__':
  import xmlrunner
  runner = xmlrunner.XMLTestRunner(output='test-reports')
  unittest.main(testRunner=runner)
  unittest.main()
