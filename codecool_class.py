from mentor import Mentor
from student import Student


class CodecoolClass:

    def __init__(self, location, year, mentors, students):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students

    def generate_local(location, year, mentors, students):
        cc_budapest = CodecoolClass("Budapest", 2016, Mentor.count_names(), Student.count_names())
        return cc_budapest

    def find_student_by_full_name(full_name):
        if full_name in Student.create_full_name_list():
            print("{} was found between the students".format(full_name))
        else:
            print("{} was not found between the students".format(full_name))

    def find_mentor_by_full_name(full_name):
        if full_name in Mentor.create_full_name_list():
            print("{} was found between the mentors".format(full_name))
        else:
            print("{} was not found between the mentors".format(full_name))
