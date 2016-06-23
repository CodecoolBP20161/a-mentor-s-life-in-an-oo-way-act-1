from mentor import Mentor
from student import Student


class Feedback():

    def __init__(self, mentor_name):
        self.mentor_name = mentor_name

    def give_feedback(self, person_object):
        person_object.knowledge_level += 5
        person_object.joy_level += 5
        print(
            "{0} gave a compliment to {1}, so {1}'s knowledge and joy level increased by 5".format(
                self.mentor_name,
                person_object.nickname))

    @staticmethod
    def get_feedback(mentor_object):
        mentor_object.energy_level += 5
        mentor_object.joy_level += 5
        print(
            "{0} asked the students for some feedback. {0}'s energy and joy level increased by 5".format(
                mentor_object.nickname))
