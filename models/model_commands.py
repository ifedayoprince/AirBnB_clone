#!/usr/bin/python3

from models import storage

class ModelCommands:
    def __init__(self, class_name):
        self.class_name = class_name

    def count(self):
        print(len([x for x in storage.all().values()
                  if x.__class__.__name__ == self.class_name]))
        return False

    def all(self):
        print([str(x) for x in storage.all().values()
                  if x.__class__.__name__ == self.class_name])
        return False

    def show(self, *args):
        if len(args) < 1:
            print("** instance id missing **")
            return False

        key = f"{self.class_name}.{args[0]}"
        if key not in storage.all():
            print("** no instance found **")
            return False

        obj = storage.all()[key]
        print(obj)

    def destroy(self, *args):
        if len(args) < 1:
            print("** instance id missing **")
            return False

        key = f"{self.class_name}.{args[0]}"
        if key not in storage.all():
            print("** no instance found **")
            return False

        storage.all().pop(key)
        storage.save()

    def update(self, *args):
        if len(args) < 1:
            print("** instance id missing **")
            return False

        elif len(args) >= 2:
            if type(args[1]) is dict:
                key = f"{self.class_name}.{args[0]}"
                if key not in storage.all():
                    print("** no instance found **")
                    return False

                obj = storage.all()[key]
                for key, value in args[1].items():
                    setattr(obj, key, value)
                storage.save()
                return False

        elif len(args) < 2:
            print("** attribute name missing **")
            return False

        elif len(args) < 3:
            print("** value missing **")
            return False

        key = f"{self.class_name}.{args[0]}"
        if key not in storage.all():
            print("** no instance found **")
            return False

        obj = storage.all()[key]
        setattr(obj, args[1], args[2])
        storage.save()