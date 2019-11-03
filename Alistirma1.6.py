#ilk rakami son rakaminden büyük olan kac tane 4 basamakli sayi oldugunu verir

counter=0
for i in range(1000,10000):
     i=str(i)
     if(int(i[0])>int(i[3])):
          counter=counter+1
print(counter)
