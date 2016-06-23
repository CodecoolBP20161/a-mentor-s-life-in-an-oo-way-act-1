from mentor import Mentor
from student import Student


class Electronic():

    def __init__(self, name, switch, error):
        self.name = name
        self.switch = switch
        self.error = error

    def tool_switcher(self):
        if self.error is False:
            if self.switch is True:
                self.switch = False
                print("The tool is switched OFF")
            else:
                self.switch = True
                print("The tool is switched ON")
        else:
            print("The tool doesn't working! :(")

    def tool_repair(self, mentor_object):
        if self.error is True:
            self.error = False
            print("The tool is working now! :)")
            mentor_object.knowledge_level += 20
            print("{}'s knowledge level increasing by 20 (It was a vluable experiance!)". format(
                mentor_object.nickname))
            mentor_object.energy_level -= 15
            print("{}'s energy level decreasing by 15. (It was very exhausting...)". format(
                mentor_object.nickname))
        else:
            print("The tool already working!")


class Laptop(Electronic):
    def __init__(self, name, switch, error):
        super().__init__(name, switch, error)

    def coding(self, student_object):
        if self.switch is True:
            student_object.knowledge_level += 10
            student_object.energy_level -= 10
            print("{}'s knowledge level increasing and the energy level decreasing by 10.". format(
                student_object.nickname))
        else:
            print("The laptop isn't turned on.")
        return

    def playing(self, student_object):
        if self.switch is True:
            student_object.joy_level += 10
            student_object.energy_level -= 10
            print("{}'s joy level increasing and the energy level decreasing by 10.". format(
                student_object.nickname))
        else:
            print("The laptop isn't turned on.")
        return
