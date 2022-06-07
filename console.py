#!/usr/bin/python3
"""Defines the AirBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB command interpreter."""
    prompt = "hbnb "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exits the program on receiving end-of-file signal."""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
