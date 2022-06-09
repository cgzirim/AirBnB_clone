#!/usr/bin/python3
"""Defines the AirBnB console."""
import re
import cmd
from shlex import split

from click import argument
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


CLASSES = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


def parse(arg):
    """Splits arguments passed in arg into a list"""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[: brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[: curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB command interpreter."""

    prompt = "hbnb "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def default(self, arg):
        """Default behavior for cmd module when input is invalid."""
        cmds = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }
        if "." in arg and "(" in arg and ")" in arg:
            cls = arg[: arg.index(".")]
            method = arg[arg.index(".") + 1 : arg.index("(")]
            argument = arg[arg.index("(") + 1 : arg.index(")")]
            argument = "{} {}".format(cls, argument.replace(",", ""))
            # print(argument)
            # return
            if method in cmds.keys():
                return cmds[method](argument)
        self.stdout.write("*** Unknown syntax: %s\n" % arg)
        return

    def do_EOF(self, arg):
        """On receiving end-of-file signal, exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel

        Usage: create <class> or <class>.create()
        """
        args = parse(arg)
        print(args[0])
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id.

        Usage: show <class> <id> or <class>.show()
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all()[key]
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            key = "{}.{}".format(args[0], args[1])
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name.

        Usage: all or all <class> or <class>.all()
        Ex: (hbnb) all
            (hbnb) all BaseModel
        """
        args = parse(arg)
        if len(args) > 0:
            if args[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                for key, obj in storage.all().items():
                    if args[0] in key:
                        print(obj)
        else:
            for key, obj in storage.all().items():
                print(obj)

    def do_count(self, arg):
        """Retrieves the number of instances of a class.

        Usage: count <class_name> or <class_name>.count()
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            count = 0
            for key in storage.all().keys():
                if arg[0] in key:
                    count += 1
            print(count)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>" or
                <class name>.update(<id>, <attribute name>, <attribute value>)
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        else:
            if len(args) < 4:
                try:
                    if type(eval(args[2])) != dict:
                        return
                except NameError:
                    print("** value missing **")
                    return False

            key = "{}.{}".format(args[0], args[1])
            obj = storage.all()[key]
            if args[2] not in ["id", "created_at", "updated_at"]:
                if len(args) == 4:
                    # if the attribute already exist, cast the value to the
                    # attribute type.
                    value = args[3]
                    if args[2] in obj.__dict__.keys():
                        value = type(obj.__dict__[args[2]])(args[3])
                    setattr(obj, args[2], value)
                else:  # args[3] is a dictionary
                    for k, v in eval(args[2]).items():
                        if k in obj.__dict__.keys() and type(
                            obj.__class__.__dict__[k] in {str, int, float}
                        ):
                            valtype = type(obj.__dict__[k])
                            setattr(obj, k, valtype(v))
                        else:
                            setattr(obj, k, v)
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
