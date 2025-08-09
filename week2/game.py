import random
def game():
    list = ["apple", "banana", "cherry", "date", "elderberry"]
    a=random.choice(list)
    b=len(a)
    word = [' ' for i in range(b)]
    print("let's guess the letter, you can enter a letter")
    num=0
    i=0
    life=10
    while num<b:
        letter=input()[0]
        for i in range(0,b):
            if letter==a[i] and word[i]==' ':
                num=num+1
                word[i]=letter
                print("correct,the word is ",word)
                if ''.join(word)==a:
                    print("you win")
                break
            if i==b-1:
                life=life-1
                print("wrong letter, you only have",life," of life")
            if life==0:
                return print("you lose")
game()
