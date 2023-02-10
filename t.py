n=int(input())
v=n%18
if v>=1 and v<=6:
    print("asal")
elif v>=7 and v<=12:
    print("skolad")
elif v>=13 and v<=16:
    print('chiz')
elif v==17 or v == 0:
    print('yoq')