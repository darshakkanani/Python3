import random

test_seed = int(input("Input seed number: "))

random.seed(test_seed)

x = random.randint(1,10)
print(x)
