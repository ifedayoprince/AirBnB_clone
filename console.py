#!/usr/bin/python3
"""
Command interpreter for the AirBnB clone.
"""

from models.classes import models
import cmd
import shlex
from models import storage
import re
from models.model_commands import ModelCommands


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for AirBnB clone.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in models:
            print("** class doesn't exist **")
            return False

        obj = models[args[0]]()
        obj.save()
        print(obj.id)
        return False

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in models:
            print("** class doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return False

        obj = storage.all()[key]
        print(obj)
        return False

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in models:
            print("** class doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return False

        storage.all().pop(key)
        storage.save()
        return False

    def do_all(self, line):
        """
        Prints all string representation of all instances
        Usage: all <class name>
        """
        args = shlex.split(line)
        if len(args) == 0:
            print([str(x) for x in storage.all().values()])
            return False
        elif args[0] not in models:
            print("** class doesn't exist **")
            return False

        print([str(x) for x in storage.all().values()
              if x.__class__.__name__ == args[0]])
        return False

    def do_update(self, line):
        """
        Updates an instance based on the class name
           and id by adding or updating attribute
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in models:
            print("** class doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False
        elif len(args) < 3:
            print("** attribute name missing **")
            return False
        elif len(args) < 4:
            print("** value missing **")
            return False

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return False

        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        storage.save()
        return False

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

    def do_help(self, arg):
        """
        Help command to display help for commands.
        """
        if arg:
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, 'do_' + arg).__doc__
                    if doc:
                        self.stdout.write(f"{str(doc.strip())}\n\n")
                        return
                except AttributeError:
                    pass
                self.stdout.write("%s\n" % str(self.nohelp % (arg,)))
                return
            func()
        else:
            cmd.Cmd.do_help(self, arg)

    def default(self, line):
        """Handle unrecognized commands"""
        match = re.match(r"(\w+)\.(show|update|all|count|destroy)\(.*\)", line)
        if match:
            class_name = match.group(1)

            if class_name not in models:
                print("** class doesn't exist **")

            action = line.strip().split(".")[1]
            try:
                eval(f"ModelCommands('{class_name}').{action}")
            except:
                print(f"** Unknown syntax: {line}")
        else:
            print(f"** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
