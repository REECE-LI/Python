""" 游戏改进 """


import random

answer = random.randint(1, 10)

counts = 3

while counts > 0:
    
    temp = input("猜一个数")
    guess = int(temp)

    if guess == answer:
        print("Right!")
        break
    else:
        if guess < answer:
            print("small")
            
        else:
            print("big")
    counts -= 1
            
    
print("game over")
