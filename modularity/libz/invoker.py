import os
import sys

PACKAGE_PARENT = '../..'  # noqa # nopep8
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))  # noqa # nopep8
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))  # noqa # nopep8


from modularity.libz.greetings import get_hello_message
from modularity.libz.farewells import get_goodbye_message


def main():
    print(get_hello_message())
    print(get_goodbye_message())


main()
