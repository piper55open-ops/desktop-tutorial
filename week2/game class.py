import random

class Game:
    def __init__(self):
        self.list = ["apple", "banana", "cherry", "date", "elderberry"]
        self.a = random.choice(self.list)
        self.len = len(self.a)
        self.word = [' ' for _ in range(self.len)]
        self.num = 0
        self.life = 10

    def play(self):
        while self.num < self.len and self.life > 0:
            print("Let's guess the letter, you can enter a letter:")
            letter = input()[0]
            if self.check(letter):
                print("Correct! The word is", self.word)
                if ''.join(self.word) == self.a:
                    print("You win!")
                    return
            else:
                self.life -= 1
                print(f"Wrong letter, you only have {self.life} lives left")
        print(f"You lose! The word was '{self.a}'")

    def check(self, letter):
        found = False
        for i in range(0,self.len):
            if letter == self.a[i] and self.word[i] == ' ':
                self.word[i] = letter
                self.num += 1
                found = True
        return found

game = Game()
game.play()
