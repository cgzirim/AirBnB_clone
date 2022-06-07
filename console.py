#!/usr/bin/python3
"""Implement shell like command line interpreter with python cmd module"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "hbnb "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self):
        """Exits the program on receiving end-of-file signal."""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
