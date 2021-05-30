import os
import sys

from dotenv import load_dotenv

# Here we are pointing to the repository root
PACKAGE_PARENT = '../..'  # noqa # nopep8
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))  # noqa # nopep8
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))  # noqa # nopep8


from modularity.libz.greetings import get_hello_message
from modularity.libz.farewells import get_goodbye_message


load_dotenv()


def main():
    user = os.environ.get('USER_NAME')
    print(get_hello_message(user))

    print(get_goodbye_message(user))


main()
