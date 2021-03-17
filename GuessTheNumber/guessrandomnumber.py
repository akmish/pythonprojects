import random

def guessthenumber(x):
    random_num = random.randint(1, x)
    guessthenumber = 0
    count = 0
    print ("Let's play a game, Guess The Number!!")
    while guessthenumber != random_num:
        guessthenumber = int(input(f"Choose a number between 1 and {x}: "))
        if guessthenumber > random_num:
            print("Your guess is too high..")
        elif guessthenumber < random_num:
            print("Your guess is too low..")
        count += 1

    print(f"Congratulation!!! You gussed our random number corectly {random_num} correctly in {count} times")


guessthenumber(10)