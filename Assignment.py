import datetime
from mentor import Mentor


class Assignment:
    def __init__(self, name, difficulty, due_hour):

        self.name = name
        self.difficulty = difficulty
        self.due_hour = int(due_hour)

    def check_assignment(self, mentor_object):
        actual_time_hour = datetime.datetime.now().hour
        remain_time = self.due_hour - actual_time_hour
        if self.due_hour < int(actual_time_hour):
            print("{0} corrected {1} assignment.".format(mentor_object.nickname, self.name))
            return mentor_object.joy += 5
        else:
            print("There's still {} hours until the end of the deadline.".format(remain_time))

helloworld = Assignment("helloworld", "beginner", "9")
helloworld.check_assignment("Miki")
