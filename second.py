
import random

n=input("Please input a num:") #请输入整数

print("{:->20}".format(eval(n)))

random.seed(123) #以123为种子生成随机数
for i in range(10):
    print(random.randint(1,999),end=",")
print()

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[3,6,9]

s=0

for c in a:
    for j in range(3):
        s+=c[j]*b[j]
print("总和为：",s)

s2=input("please input a string:")
print("{:=^15}".format(s2[0:15]))
