import os

MAKS = 100

def MenuPilihan():
    os.system('cls')
    print("=== MENU GUDANG ===")
    print("1. Urut Barang")
    print("2. Lihat Data Barang")
    print("0. Keluar")
    Pilih = int(input())
    return Pilih

def MenuUrutBarang():
    os.system('cls')
    print("=== MENU URUT BARANG ===")
    print("1. Kode Barang")
    print("2. Nama Barang")
    print("3. Jenis Barang")
    print("4. Stok Barang")
    print("0. Keluar")
    Pilih2 = int(input())
    return Pilih2

def JenisBarang(KodeBrg):
    if KodeBrg[:3] == "000":
        return "Mainan"
    elif KodeBrg[:3] == "100":
        return "Perlengkapan Mandi"
    elif KodeBrg[:3] == "200":
        return "Alat Tulis"
    elif KodeBrg[:3] == "300":
        return "Minuman"
    elif KodeBrg[:3] == "400":
        return "Makanan Ringan"
    else:
        return "Tidak Diketahui"

def IsiDataBarang(KodeBrg, NamaBrg, JenisBrg, StokBrg):
    os.system('cls')
    i = 0
    print("PENGISIAN DATA BARANG")
    print("======================")
    print(f"Data Barang Ke-{i+1}")
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
        print(f"Data Barang Ke-{i+1}")
        Kode = input('Kode Barang = ')
    N = i
    return N

def UrutKodeAsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if KodeBrg[j] < KodeBrg[j-1]:
                
                TempStr = KodeBrg[j]
                KodeBrg[j] = KodeBrg[j-1]
                KodeBrg[j-1] = TempStr
                
                TempStr = NamaBrg[j]
                NamaBrg[j] = NamaBrg[j-1]
                NamaBrg[j-1] = TempStr
                
                TempStr = JenisBrg[j]
                JenisBrg[j] = JenisBrg[j-1]
                JenisBrg[j-1] = TempStr
                
                TempInt = StokBrg[j]
                StokBrg[j] = StokBrg[j-1]
                StokBrg[j-1] = TempInt

def UrutNamaDsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    for i in range(N-1):
        for j in range(N-1-i):
            if NamaBrg[j] < NamaBrg[j+1]:
                
                TempStr = KodeBrg[j]
                KodeBrg[j] = KodeBrg[j+1]
                KodeBrg[j+1] = TempStr
                
                TempStr = NamaBrg[j]
                NamaBrg[j] = NamaBrg[j+1]
                NamaBrg[j+1] = TempStr
                
                TempStr = JenisBrg[j]
                JenisBrg[j] = JenisBrg[j+1]
                JenisBrg[j+1] = TempStr
                
                TempInt = StokBrg[j]
                StokBrg[j] = StokBrg[j+1]
                StokBrg[j+1] = TempInt

def UrutJenisAsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    for i in range(N-1):
        Min = i
        for j in range(i+1, N):
            if JenisBrg[j] < JenisBrg[Min]:
                Min = j
        
        TempStr = KodeBrg[Min]
        KodeBrg[Min] = KodeBrg[i]
        KodeBrg[i] = TempStr
        
        TempStr = NamaBrg[Min]
        NamaBrg[Min] = NamaBrg[i]
        NamaBrg[i] = TempStr
        
        TempStr = JenisBrg[Min]
        JenisBrg[Min] = JenisBrg[i]
        JenisBrg[i] = TempStr
        
        TempInt = StokBrg[Min]
        StokBrg[Min] = StokBrg[i]
        StokBrg[i] = TempInt

def UrutStokDsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    for i in range(N-1):
        Max = i
        for j in range(i+1, N):
            if StokBrg[j] > StokBrg[Max]:
                Max = j
        
        TempStr = KodeBrg[Max]
        KodeBrg[Max] = KodeBrg[i]
        KodeBrg[i] = TempStr
        
        TempStr = NamaBrg[Max]
        NamaBrg[Max] = NamaBrg[i]
        NamaBrg[i] = TempStr
        
        TempStr = JenisBrg[Max]
        JenisBrg[Max] = JenisBrg[i]
        JenisBrg[i] = TempStr
        
        TempInt = StokBrg[Max]
        StokBrg[Max] = StokBrg[i]
        StokBrg[i] = TempInt

def TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg):
    os.system('cls')
    print("===============================================")
    print(" NO | KODE BARANG | NAMA BARANG | JENIS | STOK ")
    print("===============================================")
    for i in range(N):
        print(f"{i+1:2} | {KodeBrg[i]:11} | {NamaBrg[i]:11} | {JenisBrg[i]:10} | {StokBrg[i]:4}")
    print("===============================================")
    os.system('pause')

KodeBrg = ["/"] * MAKS
NamaBrg = ["/"] * MAKS
JenisBrg = ["/"] * MAKS
StokBrg = [0] * MAKS
N = IsiDataBarang(KodeBrg, NamaBrg, JenisBrg, StokBrg)
Pilih = MenuPilihan()
while Pilih != 0:
    if Pilih == 1:
        if N > 0:
            Pilih2 = MenuUrutBarang()
            while Pilih2 != 0:
                if Pilih2 == 1:
                    UrutKodeAsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                    TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                elif Pilih2 == 2:
                    UrutNamaDsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                    TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                elif Pilih2 == 3:
                    UrutJenisAsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                    TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                elif Pilih2 == 4:
                    UrutStokDsc(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                    TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
                else:
                    print("Menu tidak ada!")
                    os.system('pause')
                Pilih2 = MenuUrutBarang()
        else:
            print("Isi data barang terlebih dahulu")
            os.system('pause')
    elif Pilih == 2:
        if N > 0:
            TampilDataBarang(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
        else:
            print("Isi data barang terlebih dahulu")
            os.system('pause')
    else:
        print("Menu tidak ada!")
        os.system('pause')
    Pilih = MenuPilihan()