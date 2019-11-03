
min_fark=121212
for i in range(1,int(121212**0.5)+1):
    for j in range(int(121212**0.5)+1,121213):
        if(i*j==121212):
            fark=j-i
            if(fark<min_fark):
                min_fark=fark
                i_istenen=i
                j_istenen=j
print(i_istenen,j_istenen)
            
