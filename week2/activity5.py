import string
class getword:
    def __init__(self):
        print("say something")
        self.sentence=input("")
        self.length=len(self.sentence)
        self.num=0
        self.all_letters = string.ascii_letters
    def findword(self):
        for i in range(0,self.length):
            if self.sentence[i] not in self.all_letters:
                self.num=self.num+1
            if i==self.length-1 and self.sentence[self.length-1] in self.all_letters:
                self.num = self.num + 1
        return print(self.num)
a=getword()
a.findword()
