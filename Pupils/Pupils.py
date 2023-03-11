class Pupil:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age


pupils = []


def print_class(pupils):
    for pupil in pupils:
        print(pupil.Name, "-", pupil.Age)
    print("\n")


def find_eldest(pupils):
    Eldest_Pupil = Pupil("", 0)
    for pupil in pupils:
        if pupil.Age > Eldest_Pupil.Age:
            Eldest_Pupil.Age = pupil.Age
            Eldest_Pupil.Name = pupil.Name
    return Eldest_Pupil


def get_average_age(pupils):
    sum = 0
    for pupil in pupils:
        sum += pupil.Age
    sum /= len(pupils)
    return sum


with open("pupils_txt.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.split(" ")
        pupil = Pupil(data[0], int(data[1]))
        pupils.append(pupil)

print_class(pupils)
Eldest_Pupil = find_eldest(pupils)
Average_Age = get_average_age(pupils)

print("Старший ученик:", Eldest_Pupil.Name, " - ", Eldest_Pupil.Age, "\nСредний возраст группы:", Average_Age)