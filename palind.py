n=int(input())
s=input()
s1=''
for i in s:
    s1=s1+i
    a=len(s) if s1==s1[::-1] else 1
print(a)