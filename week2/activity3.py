class daxie:
    def __init__(self, text):
        self.text = text

    def transform(self):
        uppertext = self.text.upper()
        return print(uppertext)

    def find_character(self, char):
        return self.text.find(char)

    def lenth(self):
        return print(len(self.text))


name = daxie("example")
name.transform()
name.lenth()
result = name.find_character('a')
print(result)
