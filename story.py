from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student

miki = Mentor.create_by_csv()[0]
dani = Mentor.create_by_csv()[1]
tomi = Mentor.create_by_csv()[2]

móni = Student.create_by_csv()[0]
