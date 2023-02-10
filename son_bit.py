"""
math.lcm()  #EKUK
math.gcd()  #EKUB
"""
n=int(input())

a=0
for i in range(n):
    c=bin(i)
    d=c.count('1')
    if n==(d+i):
        a=i
        break
    else:
        a=-1
        
print(a)