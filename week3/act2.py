import string
class count:
    def __init__(self):
        self.num = 0
        self.all_letters = string.ascii_letters
        self.file = open('demo (1).txt', 'r', encoding='utf-8')
        self.text = self.file.read()
        self.length = len(self.text)
    def findword(self):
        for i in range(0,self.length):
            if self.text[i] not in self.all_letters and i > 0 and self.text[i - 1] in self.all_letters:
                self.num += 1
            if i == self.length - 1 and self.text[i] in self.all_letters:
                self.num += 1
        return print(f"There are a total of {self.num} words in the demo file.")
a=count()
a.findword()
