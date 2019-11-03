




maks_kalan=0
Kalan=0
for X in range(1,125):
    if((125%X==200%X)and(200%X==350%X)):
        Kalan=125%X
        
        if(Kalan>=maks_kalan):
            maks_kalan=Kalan
            X_istenen=X
print(X_istenen)

        


