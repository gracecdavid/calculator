import unittest

from calculator import helloworld

class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        hello = helloworld()
        self.assertEqual(hello, "Hello world of Python\n")


