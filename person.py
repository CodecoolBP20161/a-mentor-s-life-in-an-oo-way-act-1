class Person:

    GENDER_TYPE = ["male", "female", "notsure"]

    def __init__(self, first_name=None, last_name=None, year_of_birth=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender

    def is_attribute(self):
        try:
            if isinstance(first_name, Person):
                if self.first_name == str(self.first_name):
                    pass
                else:
                    raise AttributeError
            elif isinstance(last_name, Person):
                if self.last_name == str(self.last_name):
                    pass
                else:
                    raise AttributeError
            elif isinstance(year_of_birth, Person):
                if self.year_of_birth == int(self.year_of_birth):
                    pass
                else:
                    raise AttributeError
            elif isinstance(gender, Person):
                if self.last_name == str(self.gender) and self.gender in GENDER_TYPE:
                    pass
                else:
                    raise AttributeError
        except AttributeError:
            raise AttributeError
