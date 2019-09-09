#APLIKASI PARKIR ( jam parkir < 24 JAM)

#RULES:
#PILIHAN INPUT : pagi dan malam (sistem 12 jam)
#TARIF PARKIR   : 
#   3jam pertama    : 3000/Jam
#   > 3 jam pertama : 1000/jam
#   maksimal tarif  : 25000


#INPUT DATA
check = False
while (check == False):
    masuk1 = input('Jam Masuk (1-12): ')
    if(masuk1.isdigit() == True):
        masuk1 = int(masuk1)
        if(masuk1 > 0 and masuk1 < 13):
            check = True 
        else: 
            print('Inputan salah, angka 1 - 12 saja!')
    else:
        print('Inputan salah, masukkan angka!')

    masuk2 = input('Pagi atau Malam  : ')
    masuk2 = masuk2.lower()
    if(masuk2.isalpha() == True):
        if (masuk2 == 'pagi' and 'malam'):
            check = True
        else:
            print('Inputan salah, masukkan Pagi / Malam')
    else:
        print('Inputan salah, masukkan Pagi / Malam')

check = False
while (check == False):    
    keluar1 = input('Jam Keluar (1-12): ')
    if(keluar1.isdigit()==True):
        keluar1 = int(keluar1)
        if (keluar1 > 0 and keluar1 <13):
            check = True
        else:
            print('Inputan salah')
    keluar2 = input('Pagi atau Malam : ')
    keluar2 = keluar2.lower()
    if(keluar2.isalpha() == True):
        if (keluar2 == 'pagi' and 'malam'):
            check = True
        else:
            print('Inputan salah, masukkan Pagi / Malam')
    else:
        print('Inputan salah, masukkan Pagi / Malam')


#VARIABEL PENGKONDISIAN
kondisi1 = keluar2 == masuk2 and keluar1 > masuk1
kondisi2 = keluar2 == masuk2 and keluar1 < masuk1
kondisi3 = keluar2 != masuk2


#PROCESS
if(kondisi1):
    jam = keluar1 - masuk1
    if(jam < 4):
        harga = jam*3000
    elif(3 < jam):
        harga = (3*3000)+((jam-3)*1000)
elif(kondisi2):
    jam = 12 + keluar1 + (12-masuk1) 
    if(jam < 20):
        harga = (3*3000)+((jam-3)*1000)
    elif(19 < jam):
        harga = 25000
elif(kondisi3):
    jam = (12-masuk1)+keluar1
    if(jam < 4):
        harga = jam*3000
    elif(3 < jam < 20):
        harga = (3*3000)+((jam-3)*1000)
    elif(19 < jam):
        harga = 25000


#OUTPUT
print('Anda parkir selama ' + str(jam) + ' jam, anda harus bayar ' + str(harga))
