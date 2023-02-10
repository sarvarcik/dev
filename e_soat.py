n=input()

soat=int(n)//3600
minut=(int(n)-soat*3600)//60
sec=int(n)-soat*3600 - minut*60

soat2=soat if soat<=23 else soat%24
minut2=minut if minut>=10 else "0" + str(minut)
sec2=sec if sec>=10 else "0" + str(sec)

print(f'{soat2}:{minut2}:{sec2}')