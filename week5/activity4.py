class Human(object):
    def __init__(self, name, address, age, ID):
        self.name = name
        self.address = address
        self.age = age
        self.ID = ID

    def say(self):
        print(f"{self.name}  {self.address}")


class Student(Human):
    def __init__(self, name, address, age, ID, academicrecord):
        super().__init__(name, address, age, ID)
        self.academicrecord = academicrecord
    def say(self):
        print(f"{self.name}  {self.ID} {self.academicrecord}")


class Academics(Human):
    def __init__(self, name, address, age, ID, taxcode, salary):
        super().__init__(name, address, age, ID)
        self.taxcode = taxcode
        self.salary = salary

    def say(self):
        print(f"{self.name}  {self.taxcode} {self.salary}")


class Staff(Human):
    def __init__(self, name, address, age, ID, taxcode, payrate):
        super().__init__(name, address, age, ID)  
        self.taxcode = taxcode
        self.payrate = payrate

    def say(self):
        print(f"{self.name} {self.payrate}")


if __name__ == '__main__':
    c = Student('LI JIU YU', 'fugou', '25', '66', '123')
    d = Academics('LI BEN WEI', 'HENAN', '40', '123', '456', '789')
    e = Staff('WANG ER', 'BEIJING', '30', '777', '888', '50')
    c.say()
    d.say()
    e.say()
    f = Human('ding ding', 'shanghai', '35', '999')
    f.say()
