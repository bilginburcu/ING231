#1'den N'ye kadar olan sayilarin toplamini rekürsif olarak yazan fonksiyon

N=int(input("Bir sayi giriniz:"))


def rekursif_toplama(N):
    if(N==1):
        return 1
    else:
        return N+rekursif_toplama(N-1)


print(rekursif_toplama(N))
