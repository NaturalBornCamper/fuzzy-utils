from json import dumps
from sys import stdout

from pyrotools import _constants


class COLORS(_constants.COLORS):
    pass


def cprint(color, *values):
    print(color, end="", flush=True)
    for value in values:
        print(value, end=" ", flush=True)
    print(COLORS.RESET)


def pprint(var):
    print(dumps(var, sort_keys=True, indent=3))


def cpprint(color, var):
    print(color, end="", flush=True)
    pprint(var)
    print(COLORS.RESET)


def query_yes_no(question, default="no", color=_constants.COLORS.RESET):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        stdout.write(color + question + COLORS.RESET + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")
