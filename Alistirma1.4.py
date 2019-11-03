#3 basamakli tüm palindromik sayileri bulup ekrana basar

for i in range(100,1000):
    i=str(i)
    if(int(i[0])==int(i[-1])):
        print(i)

        
