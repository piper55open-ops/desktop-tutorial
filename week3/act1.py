class wenjian:
    def __init__(self):
        self.file = open('demo (1).txt', 'a', encoding='utf-8')
    def write(self):
        with open("text.txt", "a", encoding='utf-8'):
            self.file.write("I am learning Python!\n")
        self.file.close()
    def read(self):
        file = open('demo (1).txt', 'r', encoding='utf-8')
        try:
            text = file.read()
            print(type(text))
            print(text)
        finally:
            file.close()
a=wenjian()
a.read()
