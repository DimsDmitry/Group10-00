class Pupil:
    def __init__(self, surname, name, otcenka):
        self.surname = surname
        self.name = name
        self.otcenka = otcenka


pupils = []
otl = []
f = open('pupils_txt.txt', 'r')
lines = f.readlines()
cre_otc = 0

for w in lines:
    fio = w.split()
    p = Pupil(fio[0], fio[1], fio[2])
    print(p.surname, p.name, p.otcenka)
    pupils.append(p)
    if fio[2] == '5':
        otl.append(p)
    cre_otc = cre_otc + int(fio[2])

print('\n отличники:')
for w in otl:
    print(w.surname, w.name)

print('средняя оценка класса:', cre_otc / len(lines))
f.close()