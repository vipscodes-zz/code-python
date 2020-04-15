nilai1 = 75
nilai2 = 80

#if
if nilai1 == 75:
    print(nilai1)

if nilai1 is 75:
    print(nilai1)

if nilai2 is not 75:
    print(nilai2)

#if else
if 80 <= nilai1 <= 100:
    print("GRADE A")
else:
    print("GRADE E")

#if else if
if 80 <= nilai1 <= 100:
    print("GRADE A")
elif 60 <= nilai1 < 80:
    print("GRADE B")
elif 40 <= nilai1 < 60:
    print("GRADE C")
elif 20 <= nilai1 < 40:
    print("GRADE D")
else:
    print("GRADE E")

#nested if
if nilai1 == 75:
    print("nilai anda : ",nilai1)
    if nilai2 == 80:
        print(nilai2)


print(50*"-")
print("operator logika untuk list dan string")
mobil = ["alphard","camry","vios","innova"]
rent = "kijag"

if rent in mobil:
    print("Mobil tersedia")

if not rent in mobil:
    print("Mobil", rent, "tidak tersedia")

#CEK KARAKTER
if 'n' in rent:
    print("Ada n")
else:
    print("Tidak ada n")

