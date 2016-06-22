import datetime
from mentor import Mentor


class Assignment:
    def __init__(self, name, deadline_hour):
        self.name = name
        self.deadline_hour = int(deadline_hour)

    def check_assignment(self, mentor_object):
        actual_time_hour = datetime.datetime.now().hour
        remain_time = self.deadline_hour - int(actual_time_hour)
        if self.deadline_hour < int(actual_time_hour):
            print("{0} corrected {1} assignment.".format(mentor_object.nickname, self.name))
            mentor_object.energy -= 10
            print("{}'s energy level decreased by 10 points".format(mentor_object.nickname))
        else:
            print("There's still {} hours until the end of the deadline.".format(remain_time))
