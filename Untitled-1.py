import random
krkters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunlugu = int(input("sifrenin uzunluğunu giriniz"))
sifre = []

for i in range(sifre_uzunlugu):
    sifre += random.choice( 6krkters)

print(sifre)
