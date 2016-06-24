import datetime
from mentor import Mentor
from colors import Colors


class Assignment:
    def __init__(self, name, deadline_hour):
        self.name = name
        self.deadline_hour = int(deadline_hour)

    def check_assignment(self, mentor_object):
        actual_time_hour = datetime.datetime.now().hour
        remain_time = self.deadline_hour - int(actual_time_hour)
        if self.deadline_hour < int(actual_time_hour):
            print(Colors.OKGREEN + "{0} corrected {1} assignment."
                  .format(mentor_object.nickname, self.name) + Colors.ENDC)
            mentor_object.energy_level -= 10
            print(Colors.OKGREEN + "{}'s energy level decreased by 10 points"
                  .format(mentor_object.nickname) + Colors.ENDC)
        else:
            print(Colors.OKGREEN + "There's still {} hours until the end of the deadline."
                  .format(remain_time) + Colors.ENDC)
