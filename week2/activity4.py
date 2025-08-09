class daxie:
    def transform(self,text):
        uppertext = text.upper()
        return print(uppertext)

    def find_character(self,text ,char):
        return text.find(char)

    def lenth(self,text):
        return print(len(text))


name = daxie()
name.transform("example")
name.lenth("example")
result = name.find_character("example",'a')
print(result)
