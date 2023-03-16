import random

class Student:

    # possible values
    names = ['Vasya','Kolya','Borya','Tolya','VLADIMIR']
    surnames = ['Pupkin','Zalupkin','XyeB','kykyeB','PUTIN']
    sexs = ['man','woman']

    def __init__(self, name=None, surname=None, sex=None, age=None, height=None, weight=None):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight

    def get_random_student(self):
        self.name = random.choice(self.names)
        self.surname = random.choice(self.surnames)
        self.sex = random.choice(self.sexs)
        self.age = random.randint(17, 24)
        self.height = random.randint(150, 200)
        if self.name == 'VLADIMIR' and self.surname == 'PUTIN' and self.sex == 'man' and self.height < 160 :
            self.height = 149
            raise KeyError("Your programm was broken by KGB //._.\/._.\//._.\ Regards, BBП.")
        self.weight = random.randint(40, 150)

if __name__ == "__main__":
    # Generate group of students in set
    group = set()
    for i in range (1,30):
        student = Student()
        student.get_random_student()
        group.add(student)

    # Height analytic
    mans_count = 0
    mans_height_sum = 0
    womans_count = 0
    womans_height_sum = 0
    for student in group:
        match (student.sex):
            case 'man':
                mans_count += 1
                mans_height_sum += student.height
            case 'woman':
                womans_count += 1
                womans_height_sum += student.height
            case other:
                print(f'sorry {student.sex} {student.name}')
    print(f'Avg man\'s   height = {mans_height_sum/mans_count}')
    print(f'Avg woman\'s height = {womans_height_sum/womans_count}')

# TODO
# у каждого студента есть рюкзак (цвет, книги)
# есть ли у студента эта книга?
