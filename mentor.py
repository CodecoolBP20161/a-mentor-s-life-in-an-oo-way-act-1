from person import Person
import csv
import os


class Mentor(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname,
                 knowledge_level, energy_level, joy_level):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname
        self.knowledge_level = knowledge_level
        self.energy_level = energy_level
        self.joy_level = joy_level

    @staticmethod
    def create_by_csv():
        list_mentorobjects = []
        current_file_path = os.path.dirname(__file__)
        filereader = csv.reader(open(current_file_path + "/data/mentors.csv"), delimiter=';')
        for row in filereader:
            mentor_firstname = str(row[0]+"_mentor")
            mentor_firstname = Mentor(row[0], row[1], int(row[2]), row[3], row[4], int(row[5]), int(row[6]), int(row[7]))
            list_mentorobjects.append(mentor_firstname)
        return list_mentorobjects

    def count_names():
        current_file_path = os.path.dirname(__file__)
        filereader = csv.reader(open(current_file_path + "/data/mentors.csv"), delimiter=';')
        return sum(1 for line in filereader)

    def create_full_name_list():

        full_name_list = []

        current_file_path = os.path.dirname(__file__)
        filereader = csv.reader(open(current_file_path + "/data/mentors.csv"), delimiter=';')
        for row in filereader:
            full_name = str(row[0] + " " + row[1])
            full_name_list.append(full_name)
        return full_name_list
