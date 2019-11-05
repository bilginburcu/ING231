
#N'nin faktoriyelinin tekursif olarak hesaplanmasi
N=int(input("Faktoriyeli alinacak sayiyi giriniz: "))
def rekursif_faktoriyel(N):
    if(N==1):
        return 1
    else:
        return N*rekursif_faktoriyel(N-1)

print(N,"sayisinin faktoriyeli=",rekursif_faktoriyel(N))
