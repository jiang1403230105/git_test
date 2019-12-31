import random

n=input("Please input a num:") #请输入整数

print("{:->20}".format(eval(n)))

random.seed(123)
for i in range(10):
    print(random.randint(1,999),end=",")

