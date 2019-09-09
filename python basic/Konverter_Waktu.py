#KONVERTER WAKTU

#RULES:
#1 tahun = 360 hari
#1 bulan = 30 hari
#1 jam = 3600 detik
#1 menit = 60 detik

#INPUT, PROCESS, OUTPUT:
import math
Q1 = input('\nPilih konversi waktu: \n(1) Hari \n(2) Detik \npilih 1 atau 2 : ')
Q2 = input('\nMasukkan angka konversi : ')
Q2 = int(Q2)

if(Q1 == '1'):   
    t = (math.floor(Q2 // 360));
    b = (math.floor((Q2 % 360)/30))
    h = (math.floor(Q2 % 30));
    print (str(Q2) + ' hari sama dengan : ' + '\n' + str(t) + ' Tahun, ' + str(b) + ' Bulan, ' + str(h) + ' Hari ') 

elif (Q1 == '2'):
    j = (math.floor(Q2 // 3600));
    m = (math.floor((Q2 % 3600)/60));
    d = (math.floor(Q2 % 60));
    print(str(Q2) + ' detik sama dengan : ' + '\n' + str(j) + ' Jam, ' + str(m) + ' Menit, ' + str(d) + ' Detik')
    


