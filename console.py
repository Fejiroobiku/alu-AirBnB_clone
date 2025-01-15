#!/usr/bin/ python3

"""
HBNB Command-Line Interpreter Module

This module implements a user-friendly command-line interface for managing
HBNB objects.
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    A command-line interpreter for managing HBNB objects.
    """
    prompt = "(hbnb) "
    valid_classes = {"BaseModel": BaseModel, "User": User}

    def do_quit(self, arg):
        """
        Exit the program.
        Usage: quit
        """
        return True

    def help_quit(self):
        print("Exit the program. Usage: quit")

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl+D).
        """
        print()
        return True

    def emptyline(self):
        """
        Overrides the default behavior to do nothing on an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of a valid class and save it.
        Usage: create <class_name>
        """
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        instance = self.valid_classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """
        Display the string representation of an instance.
        Usage: show <class_name> <id>
        """
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        class_name, instance_id = args[0], (args[1] if len(args) > 1 else None)
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if not instance_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)

        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """
        Delete an instance by class name and id.
        Usage: destroy <class_name> <id>
        """
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        class_name, instance_id = args[0], (args[1] if len(args) > 1 else None)
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if not instance_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
            print(f"Deleted instance {key}")
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print string representations of all instances, optionally filtered by class.
        Usage: all [<class_name>]
        """
        args = shlex.split(arg)
        class_name = args[0] if args else None

        if class_name and class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        instances = [str(obj) for key, obj in storage.all().items()
                     if not class_name or key.startswith(class_name)]
        print(instances)

    def do_update(self, arg):
        """
        Update an instance's attribute.
        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        """
        args = shlex.split(arg)

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)

        if not instance:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name, attr_value = args[2], args[3]

        try:
            attr_value = eval(attr_value)
        except (SyntaxError, NameError):
            pass

        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
