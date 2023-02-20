#0569
n = input()
if 'P' in n or 'Q' in n or '7' in n:
  print('yes')
else:
  print('no')
  
  
#0991
n=int(input())
if n%11==0:
  print("Yes")
else:
  print("No")

  
#0605
n=int(input())
if n%3==0:
  print("Yes")
else:
  print("No")
  
  
#0549
z=input()
if (z.count("z")*2)==z.count("o"):
  print("Yes")
else:
  print("No")
  
  
#0389
a = input().split('.')
if int(a[0])<=255 and int(a[1])<=255 and int(a[2])<=255 and int(a[3])<=255:
  print('YES')
else:
  print('NO')
  
  
  
#0606
a=input()
print(int(a, base=2))


#0458
t=int(input())
for i in range(t):
  n=int(input())
  print(n*(n-1))
