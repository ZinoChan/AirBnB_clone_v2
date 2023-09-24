#!/usr/bin/python3
""" This Module contains the entry
    point of the command interpreter
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    allowed_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_quit(self, args):
        """Quits the command line"""
        return True

    def do_EOF(self, args):
        """End of File"""
        return True

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        new_instance = self.allowed_classes[args[0]]()
        for attribute_arg in args[1:]:
            key_value = attribute_arg.split("=", 1)
            if len(key_value) != 2:
                continue
            key, value = key_value
            if value[0] == '"' and value[-1] == '"':
                value = value[1:-1].replace('_', ' ').replace('\\"', '"')
            else:
                try:
                    if '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                except ValueError:
                    continue
            setattr(new_instance, key, value)

        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        instance = storage.all()
        if key in instance:
            print(instance[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based
        on the class name and id.
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        instances = storage.all()
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Displays all instances, or all
        instances of a class if specified.
        """
        args = arg.split()

        instances = storage.all()

        display_list = []

        if len(args) > 0:
            class_name = args[0]

            if class_name not in self.allowed_classes:
                print("** class doesn't exist **")
                return

            for key, instance in instances.items():
                if class_name in key:
                    display_list.append(str(instance))
        else:
            for instance in instances.values():
                display_list.append(str(instance))

        print(display_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        if attribute_name in ["id", "created_at", "updated_at"]:
            return

        attr_value = args[3].strip('"')
        try:
            attr_value = int(attr_value)
        except ValueError:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass

        setattr(instances[key], attribute_name, attr_value)
        instances[key].save()

    def do_count(self, arg):
        """
        Counts the number of instances of a specific class
        """
        count = 0
        for obj in storage.all().values():
            if arg == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        command_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        match = re.search(r"\.(\w+)\((.*?)\)$", arg)
        if match:
            class_name = arg[: match.start()]
            command = match.group(1)
            args = match.group(2).split(", ")

            if command in command_map:
                full_command = f"{command} {class_name} {' '.join(args)}"
                self.onecmd(full_command)
            else:
                print(f"{arg}: command does not exist")
        else:
            return super().default(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
