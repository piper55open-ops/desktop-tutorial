class Human(object):
    def __init__(self, name, address, age, ID):# Initialize basic human attributes
        self.name = name
        self.address = address
        self.age = age
        self.ID = ID

    def say(self):
        print(self.name, self.address)


class Student(Human):
    def __init__(self, name, address, age, ID, academicrecord):
        super().__init__(name, address, age, ID)# Call parent class constructor to initialize basic attributes
        self.academicrecord = academicrecord# Student-specific attribute: academic record


class Academics(Human):
    def __init__(self, name, address, age, ID, taxcode, salary):
        super().__init__(name, address, age, ID)# Call parent class constructor to initialize basic attributes
        self.taxcode = taxcode
        self.salary = salary


class Staff(Human):
    def __init__(self, name, address, age, ID, taxcode, payrate):
        super().__init__(name, address, age, ID)# Call parent class constructor to initialize basic attributes
        self.taxcode = taxcode
        self.payrate = payrate


if __name__ == '__main__':
    c = Student('LI JIU YU', 'fugou', '25', '66', '123')
    d = Academics('LI BEN WEI','HENAN','40','123','456','789')
    c.say()# Call the say method inherited from parent class
    d.say()
