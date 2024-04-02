class Person:
    name = 'Mary'
    age = 30
    gender = 'Female'

    def __init__(self):
        self.location = 'Nairobi'
        self.school = 'Moi University'

    def introduce(self):
        print('Persons Info:', self.name,  'Age:', self.age,'Gender:', self.gender, 'location:',self.location, 'school:', self.school)

p1 =  Person()
p1.introduce()
