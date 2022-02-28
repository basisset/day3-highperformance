from .person import Person

class Student(Person):
    def __init__(self,firstname,lastname,subject):
        Person.__init__(self,firstname,lastname)
        self.subject = subject

    def printNameSubject(self):
        return print(f'{self.firstname} {self.lastname}, {self.subject}')
        
