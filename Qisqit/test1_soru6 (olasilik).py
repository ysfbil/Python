from random import *
attempt_number=1000
heads = tails = 0
for i in range(attempt_number):
        if randrange(100) < 70: 
            heads = heads + 1 
        else: 
            tails = tails + 1

print("heads",heads/attempt_number)
print("tails",tails/attempt_number)
