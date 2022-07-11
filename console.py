#!/usr/bin/python3
"""
Class CommandConsole for Airbnb
"""
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


classes = {"BaseModel": BaseModel, "User": User, "Place": Place}
cls_up = {"State": State, "City": City, "Amenity": Amenity, "Review": Review}
classes.update(cls_up)


class HBNBCommand(cmd.Cmd):
    """
    HBNB Class
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command: exit the program """
        return True

    def do_EOF(self, line):
        """ End of File command: exit the program """
        return True

    def emptyline(self):
        """ if empty line not do nothing """
        pass

    def do_create(self, line):
        """ Metohd commnad create """
        if len(line) == 0:
            print("** class name missing **")
            return
        try:
            string = line + "()"
            instance = eval(string)
            print(instance.id)
            instance.save()
        except Exception as f:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Method commnad show """
        cmd_line = line.split()
        if len(cmd_line) == 0:
            print("** class name missing **")
            return
        elif cmd_line[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        elif len(cmd_line) == 2:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance in models.storage.all():
                print(models.storage.all()[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """ Metohd commnad destroy """
        cmd_line = line.split()
        if len(cmd_line) == 0:
            print("** class name missing **")
            return
        elif cmd_line[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        elif len(cmd_line) == 2:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance in models.storage.all():
                del models.storage.all()[instance]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """ Metohd commnad all """
        cmd_line = line.split()
        if len(cmd_line) == 0 or cmd_line[0] == "BaseModel":
            print('["', end="")
            flag = 0
            for obj_id in models.storage.all().keys():
                if flag == 1:
                    print('", "', end="")
                obj = models.storage.all()[obj_id]
                print(obj, end="")
                flag = 1
            print('"]')
        elif cmd_line[0] not in classes.keys():
            print("** class doesn't exist **")
        else:
            print('["', end="")
            # result = []
            flag = 0
            len_class = len(cmd_line[0])
            for obj_id in models.storage.all().keys():
                if obj_id[:len_class] == cmd_line[0]:
                    if flag == 1:
                        print('", "', end="")
                    obj = models.storage.all()[obj_id]
                    print(obj, end="")
                    flag = 1
            print('"]')

    def do_update(self, line):
        """ Method command update """
        cmd_line = line.split()
        keyss = ["id", "created_at", "updated_at"]
        objets = models.storage.all()
        if not line:
            print("** class name missing **")
        elif cmd_line[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        else:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance not in models.storage.all():
                print("** no instance found **")
            elif len(cmd_line) < 3:
                print("** attribute name missing **")
            elif len(cmd_line) < 4:
                print("** value missing **")
            elif cmd_line[2] not in keyss:
                obj = objets[instance]
                obj.__dict__[cmd_line[2]] = cmd_line[3]
                obj.updated_at = datetime.now()
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
