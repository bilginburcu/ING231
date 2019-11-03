#3 basamakli sayilardan ilk iki rakaminin toplami son rakamina esit olan sayilar ve adedi

counter=0
for i in range(100,1000):
    i=str(i)
    if((int(i[0])+int(i[1]))==int(i[2])):
        counter=counter+1
        print(i)

print(counter,"adet sayi vardir.")
