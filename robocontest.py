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

    
#0749
a=list(map(int,input().split()))
d=input()
a.sort()
if d=='ABC':
  print(f'{a[0]} {a[1]} {a[2]}')
elif d=='CBA':
  print(f'{a[2]} {a[1]} {a[0]}')
elif d=='BAC':
  print(f'{a[1]} {a[0]} {a[2]}')
elif d=='CAB':
  print(f'{a[2]} {a[0]} {a[1]}')
elif d=='ACB':
  print(f'{a[0]} {a[2]} {a[1]}')
elif d=='BCA':
  print(f'{a[1]} {a[2]} {a[0]}')

  
  
#0649
import datetime
k, o, y = map(int,input().split())
x = datetime.datetime(y, o, k)

d = x.strftime("%A")
print(d.upper())


#0913
v1, v2 = input().split()

print((max(abs(ord(v1[0])-ord(v2[0])), abs(int(v1[1])-int(v2[1])))+1)//2)




#0324
import math
n=int(input())
s=n-2
if n%2!=0:
    print(s)
else:
    for i in range(n):
        s-=1
        if math.gcd(n, s)==1:
            print(s)
            break

            
            
            
            
#0380
x1, y1 = input().split()
x2, y2 = input().split()
x1=ord(x1)-97
y1 = int(y1)
x2=ord(x2)-97
y2 = int(y2)
if (abs(x1-x2)==2 and abs(y1-y2)==1) or (abs(x1-x2)==1 and abs(y1-y2)==2):
  print('YES')
else:
  print('NO')
  
  
  
  
#0302
import string
h = input()
a = list(string.ascii_letters)
for i in a:
  print(i+' '+str(h.count(i)))
  
  
  
#0448
a, b, c, x = map(int,input().split())
f = a*x*x+b*x+c
if f==0:
  print('YES')
else:
  print('NO')
  
  
  
#0474
N= int(input())
if N%2==0:
  print("G'ani")
else:
  print('Ali').
  
  
  
#0772
n,k=map(int,input().split())
if 3*n>=k:
  if k>=2:
    print("YES")
  else:
    print("NO")
else:
  print("NO")
