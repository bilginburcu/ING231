
#3 basamakli cift sayilardan en az 2 rakami ayni olan sayi sayisi

counter=0
for i in range(100,1000,2):
    i=str(i)
    if((int(i[0])!=int(i[1]))and(int(i[1])!=int(i[2]))):
        0
    else:
        
        counter=counter+1

print(counter)
