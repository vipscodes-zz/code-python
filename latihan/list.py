Data = [1, 4, 9, 20, 19, 23]
#ACCESS LIST
Subdata1 = Data[0]
Subdata2 = Data[-3]
#PHARSING LIST
Subdata3 = Data[0:4]
Subdata4 = Data[4:]
Subdata5 = Data[:4]

#ADDLIST
Data1 = [1,2,3,4,5]
Data2 = [6,7,8]
Data3 = Data1 + Data2

#UPDATELIST
Data1[3] = 9
Data1[1:3] = [1,3]
#isi dari data a sama dengan Data3 (jika data a diubah maka data Data3 ikut berubah)
a = Data3

#isi dari data b sama dengan Data3 (jika data b diubah maka data Data3 tidak berubah)
b = Data3[:]

#Nested List (list multidimensi)
x = [Data1, Data2]

#akses data didalam list multidimensi
y = x[0][2]

#method menambah list
Data1.append(30)

#function untuk list
panjang_list = len(Data1)

print(panjang_list)

