#5 basamakli sayilardan ilk iki rakami son iki rakamina esit olanlarin adedini yazdirir


counter=0
for i in range(10000,100000):
    i=str(i)
    if(int(i[0]+i[1])==int(i[3]+i[4])):
    
        counter=counter+1
print(counter,"tane sayi vardir")
