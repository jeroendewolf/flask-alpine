#!/usr/bin/env python
import unittest
from app import hello

class TestApp(unittest.TestCase):
  
  def test_hello(self):
    self.assertTrue(hello() == "Hello World!")
 
if __name__ == '__main__':
  unittest.main()
