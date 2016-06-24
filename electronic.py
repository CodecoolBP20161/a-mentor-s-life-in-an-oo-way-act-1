from mentor import Mentor
from student import Student
from colors import Colors


class Electronic():

    def __init__(self, name, switch, error):
        self.name = name
        self.switch = switch
        self.error = error

    def tool_switcher(self):
        if self.error is False:
            if self.switch is True:
                self.switch = False
                print(Colors.OKGREEN + "The tool is switched OFF" + Colors.ENDC)
            else:
                self.switch = True
                print(Colors.OKGREEN + "The tool is switched ON" + Colors.ENDC)
        else:
            print(Colors.OKGREEN + "The tool doesn't work! :(" + Colors.ENDC)

    def tool_repair(self, mentor_object):
        if self.error is True:
            self.error = False
            print(Colors.OKGREEN + "The tool works now! :)" + Colors.ENDC)
            mentor_object.knowledge_level += 20
            print(Colors.OKGREEN + "{}'s knowledge level increased by 20 (It was a valuable experience!)".format(
                mentor_object.nickname) + Colors.ENDC)
            mentor_object.energy_level -= 15
            print(Colors.OKGREEN + "{}'s energy level decreased by 15. (It was very exhausting...)".format(
                mentor_object.nickname) + Colors.ENDC)
        else:
            print(Colors.OKGREEN + "The tool already works!" + Colors.ENDC)


class Laptop(Electronic):
    def __init__(self, name, switch, error):
        super().__init__(name, switch, error)

    def coding(self, student_object):
        if self.switch is True:
            student_object.knowledge_level += 10
            student_object.energy_level -= 10
            print(Colors.OKGREEN + "{}'s knowledge level increased and the energy level decreased by 10.".format(
                student_object.nickname) + Colors.ENDC)
        else:
            print(Colors.OKGREEN + "The laptop isn't turned on." + Colors.ENDC)
        return

    def playing(self, student_object):
        if self.switch is True:
            student_object.joy_level += 10
            student_object.energy_level -= 10
            print(Colors.OKGREEN + "{}'s joy level increased and the energy level decreased by 10.".format(
                student_object.nickname) + Colors.ENDC)
        else:
            print(Colors.OKGREEN + "The laptop isn't turned on." + Colors.ENDC)
        return
