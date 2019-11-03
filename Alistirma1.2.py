

#pi sayisinin yaklasik degerini hesaplar
toplam=0
for n in range (1,9999999):
    toplam=toplam+(1/(n**2))

pi= (toplam*6)**0.5
print(pi)
