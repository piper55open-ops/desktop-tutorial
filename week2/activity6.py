class hire:
    def __init__(self):
        self.name=["li jiu yu","liu hang yu","ding ding"]
        self.sallary=[50000,5000,500]
        self.position=['manager','CEO','clean']
        self.num=len(self.sallary)
        self.zhang=[""]
        self.increase=int()
        self.ask = [""]
    def display_inf(self):
            print("Whose information do you want to check?")
            self.ask = input("")
            for i in range(0, self.num):
                if self.name[i] == self.ask:
                    print("His salary is" ,self.sallary[i])
                    print("His position is" ,self.position[i])
    def give_raise(self):
        print("Who do you want to give a salary increase to? ")
        self.zhang=input("")
        print("How much do you want to increase it?")
        self.increase = int(input())
        for i in range(0, self.num):
            if self.name[i]==self.zhang:
                self.sallary[i]=self.sallary[i]+self.increase
                print("After the salary increase is", self.sallary[i])
a=hire()
a.display_inf()
a.give_raise()
