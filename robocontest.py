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
  
  
#0535
n=int(input())
if n==1 or n==2:
  print(n)
else:
  print(n*(n-1)*(n-2))

  
#0026
mod = 1000000007
t = int(input())
x = []
for i in range(t):
    n = int(input())
    x.append(n)
for i in x:
    print(i*i % mod)
    
    
    
#0027
def top(n):
    result = []
    k, j = n-1, 0
    for i in range(1,n+1):
        if i%2 == 1:
            result.append(k)
            k -= 1
        else:
            result.append(j)
            j += 1
    return result
t = int(input())
x = []
for i in range(t):
    n,k = map(int, input().split())
    x.append(top(n).index(k))
for i in x:
    print(i)
