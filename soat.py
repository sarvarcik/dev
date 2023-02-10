soat=str(input("HH:MM formatda kirit: "))
b= [soat[0], soat[1], soat[3], soat[4]]
s=0
for i in b:
    if i=='2' or i=='3' or i=='5':
        s+=5
    elif i=='6' or i=='9' or i=='0':
        s+=8
    elif i=='4':
        s+=4
    elif i=='1':
        s+=2
    elif i=='7':
        s+=3
    elif i=='8':
        s+=7
print(s)