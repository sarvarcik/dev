x=int(input())
v=0
for g in range(1,x+1):
    for i in range(1, g+1):
        v+=1 if (g%i)==0 else 0
print(v)