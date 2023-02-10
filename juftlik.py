import math
a=int(input())
b=input().split()
c=0
for i in b:
    for g in b:
        if math.gcd(int(i), int(g))==1:
            c+=1
        else:
            c+=0
print(c//2)