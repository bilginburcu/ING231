def asal_mi(b):
        c=0
        if b==2:
            return 1
        elif b==1:
            return 0
       
        for i in range(2,b):
            if(b%i==0):
                c=c+1
        if c==0:
            return 1
        else:
            return 0



for sayi in range(10000,100000):

    def sup(sayi):
        a=str(sayi)
        if len(a)==1:
            k=int(a)
            if(asal_mi(k)==0):
                return 0
            else:  
                return 1
        else:
            if (asal_mi(sayi)==1):
                
                return sup(int(a[:-1]))
            else:
                return 0
    
    if sup(sayi)==1:
        print(sayi)
