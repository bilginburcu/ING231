#4 basamakli tüm palindromik sayilari ekrana basar

for i in range(1000,10000):
    i=str(i)
    if(int(i[0]+i[1])==int(i[3]+i[2])):
        print(i)
        
