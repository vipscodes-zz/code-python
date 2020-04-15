#list iterable
mobil = ["alphard","camry","vios","innova"]

for m in mobil:
    print(m)
    print(len(m))

#string iterable
toyota = 'alphard'

for i in toyota:
    print(i)

# for didalam for (nested for)
mobil1 = ["alphard","camry","vios","innova"]
motor1 = ["beat","nmax","xmax","vario"]

daftar_kendaraan = [mobil1,motor1]
print(daftar_kendaraan)

for subDaftarKendaraan in daftar_kendaraan:
    print(subDaftarKendaraan)
    for komponen in subDaftarKendaraan:
        print(komponen)

