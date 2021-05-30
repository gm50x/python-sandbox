import os
import sys
import unittest

PACKAGE_PARENT = '../../..'  # noqa # nopep8
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))  # noqa # nopep8
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))  # noqa # nopep8

from modularity.libz.greetings import get_hello_message


class TestGreetings(unittest.TestCase):
    def test_get_hello_message_no_name(self):
        expected = 'Hello World!'
        actual = get_hello_message()
        self.assertEqual(actual, expected)

    def test_get_hello_message_name(self):
        name = 'Arthur'
        expected = f'Hello {name}!'
        actual = get_hello_message(name)
        self.assertEqual(actual, expected)
