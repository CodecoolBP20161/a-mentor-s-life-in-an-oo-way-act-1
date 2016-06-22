class Person:

    GENDER_TYPE = ["male", "female", "notsure"]

    def __init__(self, first_name=None, last_name=None, year_of_birth=None, gender=None):
        try:
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = int(year_of_birth)
            self.gender = gender
        except:
            raise AttributeError
        if self.gender not in Person.GENDER_TYPE:
            raise AttributeError("{} is not a valid gender.".format(self.gender))
