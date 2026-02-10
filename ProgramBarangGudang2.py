#Program Barang Gudang 
#{I.S.: pengguna memasukan kode barang(KodeBrg), nama barang(NamaBrg),
#       dan stok barang(StokBrg) }
#{F.S.: menampilkan hasil data barang }
import os

#konstanta
MAKS = 100

#subrutin menu pilihan
def MenuPilihan():
    os.system('cls')
    print("\033[32m=== MENU GUDANG ===\033[0m")
    print("1. Urut Barang")
    print("2. Tampil Data Barang")
    print("0. Keluar")
    Pilih = int(input("Pilih menu: "))
    return Pilih

#subrutin menu urut barang
def MenuUrutBarang():
    os.system('cls')
    print("=== MENU URUT BARANG ===")
    print("1. Kode Barang")
    print("2. Nama Barang")
    print("3. Jenis Barang")
    print("4. Stok Barang")
    print("0. Keluar")
    Pilih2 = int(input("Pilih menu: "))
    return Pilih2

#subrutin menu urut berdasarkan asc dan dsc
def MenuUrutAscDsc():
    os.system('cls')
    print("=== MENU URUT ASC/DESC ===")
    print("1. Ascending")
    print("2. Descending")
    print("0. Keluar")
    Pilih3 = int(input("Pilih menu: "))
    return Pilih3

#subrutin  jenis barang berdasarkan kode barang
def JenisBarang(KodeBrg):
    if KodeBrg[0:3] == "000":
        return "Mainan"
    elif KodeBrg[0:3] == "100":
        return "Perlengkapan Mandi"
    elif KodeBrg[0:3] == "200":
        return "Alat Tulis"
    elif KodeBrg[0:3] == "300":
        return "Minuman"
    elif KodeBrg[:3] == "400":
        return "Makanan Ringan"
    else:
        return "Tidak Diketahui"

#subrutin pengisian data barang
def IsiDataBarang(KodeBrg, NamaBrg, JenisBrg, StokBrg):
    os.system('cls')
    i = 0
    print("\033[32m======================")
    print("PENGISIAN DATA BARANG")
    print("======================\033[0m")
    print(f"Data Barang Ke-\033[31m{i+1}\033[0m")
    Kode = input('Kode Barang = ')
    while Kode != "STOP":
        KodeBrg[i] = Kode
        Nama = input('Nama Barang = ')
        NamaBrg[i] = Nama
        Jenis = JenisBarang(Kode)
        JenisBrg[i] = Jenis
        print(f"Jenis Barang = {Jenis}")
        Stok = int(input('Stok Barang = '))
        StokBrg[i] = Stok
        i += 1
        print(f"Data Barang Ke-\033[31m{i+1}\033[0m")
        Kode = input('Kode Barang = ')
    N = i
    return N

#subrutin urut kode dengan asc
def UrutKodeAsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if KodeBrg[j] < KodeBrg[j-1]:
                
                Temp = KodeBrg[j]
                KodeBrg[j] = KodeBrg[j-1]
                KodeBrg[j-1] = Temp
                
                Temp = NamaBrg[j]
                NamaBrg[j] = NamaBrg[j-1]
                NamaBrg[j-1] = Temp
                
                Temp = JenisBrg[j]
                JenisBrg[j] = JenisBrg[j-1]
                JenisBrg[j-1] = Temp
                
                Temp = StokBrg[j]
                StokBrg[j] = StokBrg[j-1]
                StokBrg[j-1] = Temp

#subrutin urut kode dengan dsc
def UrutKodeDsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if KodeBrg[j] > KodeBrg[j-1]:
                Temp = KodeBrg[j]
                KodeBrg[j] = KodeBrg[j-1]
                KodeBrg[j-1] = Temp
                
                Temp = NamaBrg[j]
                NamaBrg[j] = NamaBrg[j-1]
                NamaBrg[j-1] = Temp
                
                Temp = JenisBrg[j]
                JenisBrg[j] = JenisBrg[j-1]
                JenisBrg[j-1] = Temp
                
                Temp = StokBrg[j]
                StokBrg[j] = StokBrg[j-1]
                StokBrg[j-1] = Temp

#subrutin urut nama dengan asc
def UrutNamaAsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if NamaBrg[j] < NamaBrg[j-1]:
                Temp = KodeBrg[j]
                KodeBrg[j] = KodeBrg[j-1]
                KodeBrg[j-1] = Temp
                
                Temp = NamaBrg[j]
                NamaBrg[j] = NamaBrg[j-1]
                NamaBrg[j-1] = Temp
                
                Temp = JenisBrg[j]
                JenisBrg[j] = JenisBrg[j-1]
                JenisBrg[j-1] = Temp
                
                Temp = StokBrg[j]
                StokBrg[j] = StokBrg[j-1]
                StokBrg[j-1] = Temp

#subrutin urut nama dengan dsc
def UrutNamaDsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    for i in range(N-1):
        for j in range(N-1, i, -1): 
            if NamaBrg[j] > NamaBrg[j-1]:
                Temp = KodeBrg[j]
                KodeBrg[j] = KodeBrg[j-1]
                KodeBrg[j-1] = Temp
                
                Temp = NamaBrg[j]
                NamaBrg[j] = NamaBrg[j-1]
                NamaBrg[j-1] = Temp
                
                Temp = JenisBrg[j]
                JenisBrg[j] = JenisBrg[j-1]
                JenisBrg[j-1] = Temp
                
                Temp = StokBrg[j]
                StokBrg[j] = StokBrg[j-1]
                StokBrg[j-1] = Temp

#subrutin urut jenis dengan asc
def UrutJenisAsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    for i in range(N-1): 
        Min = i  
        for j in range(i+1, N):
            if JenisBrg[j] < JenisBrg[Min]:  
                Min = j
        
        Temp = KodeBrg[Min]
        KodeBrg[Min] = KodeBrg[i]
        KodeBrg[i] = Temp
        
        Temp = NamaBrg[Min]
        NamaBrg[Min] = NamaBrg[i]
        NamaBrg[i] = Temp
        
        Temp = JenisBrg[Min]
        JenisBrg[Min] = JenisBrg[i]
        JenisBrg[i] = Temp
        
        Temp = StokBrg[Min]
        StokBrg[Min] = StokBrg[i]
        StokBrg[i] = Temp

#subrutin urut jenis dengan asc
def UrutJenisDsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    for i in range(N-1):
        Max = i
        for j in range(i+1, N):
            if JenisBrg[j] > JenisBrg[Max]:
                Max = j
        
        Temp = KodeBrg[Max]
        KodeBrg[Max] = KodeBrg[i]
        KodeBrg[i] = Temp
        
        Temp = NamaBrg[Max]
        NamaBrg[Max] = NamaBrg[i]
        NamaBrg[i] = Temp
        
        Temp = JenisBrg[Max]
        JenisBrg[Max] = JenisBrg[i]
        JenisBrg[i] = Temp
        
        Temp = StokBrg[Max]
        StokBrg[Max] = StokBrg[i]
        StokBrg[i] = Temp

#subrutin urut stok dengan asc
def UrutStokAsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    for i in range(N-1):
        Min = i
        for j in range(i+1, N):
            if StokBrg[j] < StokBrg[Min]:
                Min = j
        
        Temp = KodeBrg[Min]
        KodeBrg[Min] = KodeBrg[i]
        KodeBrg[i] = Temp
        
        Temp = NamaBrg[Min]
        NamaBrg[Min] = NamaBrg[i]
        NamaBrg[i] = Temp
        
        Temp = JenisBrg[Min]
        JenisBrg[Min] = JenisBrg[i]
        JenisBrg[i] = Temp
        
        Temp = StokBrg[Min]
        StokBrg[Min] = StokBrg[i]
        StokBrg[i] = Temp

#subrutin urut stok dengan dsc
def UrutStokDsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    for i in range(N-1):
        Max = i
        for j in range(i+1, N):
            if StokBrg[j] > StokBrg[Max]: 
                Max = j
        
        Temp = KodeBrg[Max]
        KodeBrg[Max] = KodeBrg[i]
        KodeBrg[i] = Temp
        
        Temp = NamaBrg[Max]
        NamaBrg[Max] = NamaBrg[i]
        NamaBrg[i] = Temp
        
        Temp = JenisBrg[Max]
        JenisBrg[Max] = JenisBrg[i]
        JenisBrg[i] = Temp
        
        Temp = StokBrg[Max]
        StokBrg[Max] = StokBrg[i]
        StokBrg[i] = Temp

#subrutin menampilkan data barang
def TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    os.system('cls')
    print("=================================================================")
    print(" NO | KODE BARANG |  NAMA BARANG  |       JENIS       |  STOK  | ")
    print("=================================================================")
    for i in range(N):
        print(f"{i+1:3} | {KodeBrg[i]:11} | {NamaBrg[i]:13} | {JenisBrg[i]:18} | {StokBrg[i]:4} |")
    print("=================================================================")
    os.system('pause')

#badan program utama
KodeBrg = ["/"] * MAKS
NamaBrg = ["/"] * MAKS
JenisBrg = ["/"] * MAKS
StokBrg = [0] * MAKS
Stok = [0]
N = IsiDataBarang(KodeBrg, NamaBrg, JenisBrg, StokBrg)
Pilih = MenuPilihan()
while Pilih != 0:
    if Pilih == 1:
        if N > 0:
            Pilih2 = MenuUrutBarang()
            while Pilih2 != 0:
                if Pilih2 == 1:
                    Pilih3 = MenuUrutAscDsc()
                    while Pilih3 != 0:
                        if Pilih3 == 1:
                            UrutKodeAsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                            TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                        elif Pilih3 == 2:
                            UrutKodeDsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                            TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                        else:
                            print("Menu tidak ada!")
                            os.system('pause')
                        Pilih3 = MenuUrutAscDsc()
                elif Pilih2 == 2:
                    Pilih3 = MenuUrutAscDsc()
                    while Pilih3 != 0:
                        if Pilih3 == 1:
                            UrutNamaAsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                            TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                        elif Pilih3 == 2:
                            UrutNamaDsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                            TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                        else:
                            print("Menu tidak ada!")
                            os.system('pause')
                        Pilih3 = MenuUrutAscDsc()
                elif Pilih2 == 3:
                    Pilih3 = MenuUrutAscDsc()
                    while Pilih3 != 0:
                        if Pilih3 == 1:
                            UrutJenisAsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                            TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                        elif Pilih3 == 2:
                            UrutJenisDsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                            TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                        else:
                            print("Menu tidak ada!")
                            os.system('pause')
                        Pilih3 = MenuUrutAscDsc()
                elif Pilih2 == 4:
                    Pilih3 = MenuUrutAscDsc()
                    while Pilih3 != 0:
                        if Pilih3 == 1:
                            UrutStokAsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                            TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                        elif Pilih3 == 2:
                            UrutStokDsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                            TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                        else:
                            print("Menu tidak ada!")
                            os.system('pause')
                        Pilih3 = MenuUrutAscDsc()
                else:  
                    print("Menu tidak ada!")
                    os.system('pause')
                    os.system('cls')
                Pilih2 = MenuUrutBarang()
        else:
            print("Isi data barang terlebih dahulu")
            os.system('pause')
        N = IsiDataBarang(KodeBrg, NamaBrg, JenisBrg, StokBrg)
    elif Pilih == 2:
        if N > 0:
            TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
        else:
            print("Isi data barang terlebih dahulu")
            os.system('pause')
        N = IsiDataBarang(KodeBrg, NamaBrg, JenisBrg, StokBrg)
    else:
        print("Menu tidak ada!")
        os.system('pause')
    Pilih = MenuPilihan()