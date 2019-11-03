
for i in range(10,100):
    
    for j in range(10,100):
    
        toplam=i+j    #iki sayinin toplami
        yeni_sayi=str(i)+str(j)   #iki sayiyi yan yana getirince elde edilen 4 basamakli sayi
        if((toplam*11)==int(yeni_sayi)):
            print(i,j)
