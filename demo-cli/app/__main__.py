import argparse
import sys
import os

usage = "demo <command> [<args>]\n"

desc = """
These are common Demo commands used in various situations:

demo commands:
    command1        Print a message.
    command2        Print the current dir.
"""

class CustomParser(argparse.ArgumentParser):
    """ ArgumentParser child class to override the '-h', '--help' dialogue. """

    def format_help(self):
        return "usage: {} {}".format(self.usage, desc)

class Demo(object):
    """ Demo object class for our command-line interface. """

    def __init__(self):

        # Initialize our argparse parser, and add input option 'command'.
        parser = CustomParser(description=desc, usage=usage, formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('input', help='Subcommand to run.')

        # Parse the first argument given to your command.
        args = parser.parse_args(sys.argv[1:2])

        # Check if the object 'self' has the attribute given for 'input.'
        if not hasattr(self, args.input):
            print("Unrecognized command.")
            parser.print_help()
            exit(1)
        else:
            getattr(self, args.input)()

    def command1(self):

        # Creates secondary parser to add options to our command.
        parser = argparse.ArgumentParser()

        # Adds the flag -p for print, and will (action) store its input to (dest) args.message.
        parser.add_argument('-p', '--print', action="store", dest="message", help="Message to print.")

        # Parses all the options beyond the 2nd input.
        args = parser.parse_args(sys.argv[2:])

        if args.message is None:
            print("nothing was inputted")
        else:
            print("message: {}".format(args.message))

    def command2(self):
        # Prints the current directory of where the command was called from.
        print("working dir: {}".format(os.getcwd()))

# We initialize a main() to be called from setup.py as an entry point.
def main():
    Demo()

if __name__ == '__main__':
    main()
