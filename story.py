from assignment import Assignment
from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student


# print("The ACT present an (almost) average day in codecool.")
# skip = input()
miki = Mentor.create_by_csv()[0]
dani = Mentor.create_by_csv()[1]
tomi = Mentor.create_by_csv()[2]
# print("Mentors are initialized from CSV")
# skip = input()
móni = Student.create_by_csv()[0]
beru = Student.create_by_csv()[1]
vivi = Student.create_by_csv()[2]
beni = Student.create_by_csv()[3]
palkó = Student.create_by_csv()[4]
# print("Students are initialized from CSV")
# skip = input()
t = Assignment("test", 20)
t.check_assignment(miki)
