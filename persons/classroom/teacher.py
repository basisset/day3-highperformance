from .person import Person

class Teacher(Person):
    def __init__(self,firstname,lastname,course):
        Person.__init__(self,firstname,lastname)
        self.course = course

    def printNameCourse(self):
        return print(f'{self.firstname} {self.lastname}, {self.course}')
        


