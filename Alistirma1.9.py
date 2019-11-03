
#1'den 999'a kadar rakamlari toplami 9'dan kucuk olan sayilari yan yana yazar

for i in range(1,1000):
    if(i<10):
        if(i!=9):
            print(i,end=" ")
    elif(i<100):
        i=str(i)
        if((int(i[0])+int(i[1]))<9):
            print(i, end=" ")
    else:
        i=str(i)
        if((int(i[0])+int(i[1])+int(i[2]))<9):
            print(i, end=" ")
