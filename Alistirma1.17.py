
listem=[]

for i in range(100,1000):
    b=str(i)
    if(int(b[0])==int(b[-1])):
       listem=listem+[i]
     

for i in range(1000,10000):
    b=str(i)
    if(int(b[0]+b[1])==int(b[3]+b[2])):
        listem=listem+[i]
        




a=int(input("a="))
if a in listem:
    print(a,"palindromik.")
else:
    print(a,"palindromik degil.")
    
    


