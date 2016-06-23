from assignment import Assignment
from codecool_class import CodecoolClass
from electronic import Electronic, Laptop
from feedback import Feedback
from mentor import Mentor
from student import Student


print("The ACT present an (almost) average day in codecool.")
skip = input()
miki = Mentor.create_by_csv()[0]
dani = Mentor.create_by_csv()[1]
tomi = Mentor.create_by_csv()[2]
print("Mentors are initialized from CSV")
skip = input()
móni = Student.create_by_csv()[0]
beru = Student.create_by_csv()[1]
beni = Student.create_by_csv()[3]
print("Students are initialized from CSV")
skip = input()
print("School @ Budapest, in year 2016 is created, with 3 mentors and 4 students.")
skip = input()


print("Examine a mentor.. for example Dani.")
skip = input()
print("Nickname: {}\nKnowledge level: {}\nEnergy level: {}\nJoy level: {}".format(
    dani.nickname, dani.knowledge_level, dani.energy_level, dani.joy_level))
print("He have more attribute, but it's not necessary for now.")
skip = input()
l = Laptop("HP", False, True)
print("I created a laptop, what called {}.".format(l.name))
skip = input()
print("Then Edina try turn on. But...")
skip = input()
l.tool_switcher()
print("So she serch a mentor...")
skip = input()
print("... she found Dani. She ask his, that rapair the laptop.")
skip = input()
l.tool_repair(dani)
skip = input()
print("As we can see Dani's attribute...")
skip = input()
print("Nickname: {}\nKnowledge level: {}\nEnergy level: {}\nJoy level: {}".format(
    dani.nickname, dani.knowledge_level, dani.energy_level, dani.joy_level))
skip = input()
print("So now she can turn on the laptop.")
skip = input()
l.tool_switcher()
skip = input()
print("Finally Edina can use the laptop... So she start coding.")
skip = input()
print("Before she start coding:\nName: {}\nKnowledge level: {}\nEnergy level: {}\nJoy level: {}".format(
    beru.first_name, beru.knowledge_level, beru.energy_level, beru.joy_level))
skip = input()
l.coding(beru)
skip = input()
print("After she finished coding:\nName: {}\nKnowledge level: {}\nEnergy level: {}\nJoy level: {}".format(
    beru.first_name, beru.knowledge_level, beru.energy_level, beru.joy_level))
skip = input()

print("Meanwhile Beni play a quick game...")
skip = input()
print("Before playing:\nNickname: {}\nKnowledge level: {}\nEnergy level: {}\nJoy level: {}".format(
    beni.nickname, beni.knowledge_level, beni.energy_level, beni.joy_level))
kip = input()
l.playing(beni)
skip = input()
print("After playing:\nNickname: {}\nKnowledge level: {}\nEnergy level: {}\nJoy level: {}".format(
    beni.nickname, beni.knowledge_level, beni.energy_level, beni.joy_level))
skip = input()
print("And he win!")
skip = input()

print("During the day Móni needs a feedback...")
skip = input()
print("So she find Tomi and ask his help.")
f = Feedback("Tomi")
print("\nBefore feedback:\nNickname: {}\nKnowledge level: {}\nEnergy level: {}\nJoy level: {}".format(
    móni.nickname, móni.knowledge_level, móni.energy_level, móni.joy_level))
skip = input()
f.give_feedback(móni)
skip = input()
print("After feedback:\nNickname: {}\nKnowledge level: {}\nEnergy level: {}\nJoy level: {}".format(
    móni.nickname, móni.knowledge_level, móni.energy_level, móni.joy_level))
skip = input()

print("Sometimes a metor need a feedback too, even if his name is Miki...")
skip = input()
print("Tomi help anybody.")
print("\nBefore feedback:\nNickname: {}\nKnowledge level: {}\nEnergy level: {}\nJoy level: {}".format(
    miki.nickname, miki.knowledge_level, miki.energy_level, miki.joy_level))
skip = input()
f.get_feedback(miki)
skip = input()
print("Before feedback:\nNickname: {}\nKnowledge level: {}\nEnergy level: {}\nJoy level: {}".format(
    miki.nickname, miki.knowledge_level, miki.energy_level, miki.joy_level))
skip = input()

print("At the end of the day, Tomi check the CANVAS.")
skip = input()
a = Assignment("OOP project", 24)
a.check_assignment(tomi)
skip = input()
print("He forget, that the deadline hour don't come yet. But now he know.")
skip = input()
print("And he check an other assignment.")
skip = input()
b = Assignment("Inventory", 3)
b.check_assignment(tomi)
skip = input()
print("So the day is over, and everybody go home and rest...")
