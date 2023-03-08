#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The class that display the console"""

    prompt = '(hnhb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):
        """Handles EOF and exit the console"""

        return True

    def emptyline(self):
        """Creates an empty line that does nothing"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
