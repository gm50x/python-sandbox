import os
import sys
import unittest

PACKAGE_PARENT = '../../..'  # noqa # nopep8
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))  # noqa # nopep8
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))  # noqa # nopep8

from modularity.libz.farewells import get_goodbye_message


class TestGreetings(unittest.TestCase):
    def test_get_goodbye_message_no_name(self):
        expected = 'Goodbye World!'
        actual = get_goodbye_message()
        self.assertEqual(actual, expected)

    def test_get_goodbye_message_name(self):
        name = 'Arthur'
        expected = f'Goodbye {name}!'
        actual = get_goodbye_message(name)
        self.assertEqual(actual, expected)
