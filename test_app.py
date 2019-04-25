import app
import unittest

class TestApp:
  def test_hello(self):
    rv=self.app.get('/')
    self.assertEqual(rv.data, b'Hello World!')
 
if __name__ == '__main__':
  unitest.main()
