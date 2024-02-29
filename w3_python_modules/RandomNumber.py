# 2. Print 10 random numbers between 25 and 35 inclusively
import random
for i in range(10):
    print(random.randint(25, 36))
'''
random.randrange(25,36,2) : if you want to set different step size
random.random() : to get a random float between 0 and 1
random.uniform(25,35.00000001) : to get a float (uniformly distributed) between 25 and 35
random.choice(a_list) : to get random item from a list named a_list
'''