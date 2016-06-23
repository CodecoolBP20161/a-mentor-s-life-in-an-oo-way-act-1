from mentor import Mentor
from student import Student


class Feedback():
    def __init__(self, mentor_name):
        self.mentor_name = mentor_name

    def give_feedback(self, person_object):
        person_object.knowledge_level += 5
        person_object.joy += 5
        print("{} gave a feedback to {}.".format(self.mentor_name, person_object.name))
        print("{}'s knowledge and joy level increased by 5".format(person_object.name))
