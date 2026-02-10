import os

# --- KONSTANTA & STRUKTUR DATA (GLOBAL) ---
MAKS = 100

# --- SUBRUTIN BANTUAN ---
def BersihkanLayar():
    os.system('cls' if os.name == 'nt' else 'clear')

def TentukanJenis(KodeBrg):
    # I.S. Kode Barang terdefinisi
    # F.S. Mengembalikan string jenis barang berdasarkan prefix kode
    if KodeBrg[:3] == "000": return "Mainan"
    elif KodeBrg[:3] == "100": return "Perlengkapan Mandi"
    elif KodeBrg[:3] == "200": return "Alat Tulis"
    elif KodeBrg[:3] == "300": return "Minuman"
    elif KodeBrg[:3] == "400": return "Makanan Ringan"
    else: return "Lain-lain"

def TukarData(i, j, Kode, Nama, Jenis, Stok):
    # Subrutin untuk menukar posisi data pada index i dan j
    Kode[i], Kode[j] = Kode[j], Kode[i]
    Nama[i], Nama[j] = Nama[j], Nama[i]
    Jenis[i], Jenis[j] = Jenis[j], Jenis[i]
    Stok[i], Stok[j] = Stok[j], Stok[i]

# --- 1. PENCIPTAAN & PENAMBAHAN (INSERTION) ---
def TambahData(N, Kode, Nama, Jenis, Stok):
    # I.S. Array data dan jumlah data (N) terdefinisi
    # F.S. Data bertambah, N bertambah
    BersihkanLayar()
    print("=== TAMBAH DATA BARANG ===")
    
    if N >= MAKS:
        print("Gudang Penuh!")
        os.system('pause')
        return N

    InputKode = input("Masukkan Kode Barang (Ketik 'STOP' untuk selesai): ")
    while InputKode != "STOP" and N < MAKS:
        # Cek duplikasi kode (Validasi Data Unik)
        Ada = False
        for i in range(N):
            if Kode[i] == InputKode:
                Ada = True
                break
        
        if Ada:
            print("Error: Kode Barang sudah ada!")
        else:
            Kode[N] = InputKode
            Nama[N] = input("Masukkan Nama Barang : ")
            Jenis[N] = TentukanJenis(InputKode)
            print(f"Jenis Barang Otomatis: {Jenis[N]}")
            Stok[N] = int(input("Masukkan Stok Barang : "))
            N += 1
            print("--- Data Berhasil Disimpan ---")

        if N < MAKS:
            print(f"\nData ke-{N+1}")
            InputKode = input("Masukkan Kode Barang (Ketik 'STOP' untuk selesai): ")
        else:
            print("Memori Penuh.")
    
    return N

# --- 2. TRAVERSAL (MINIMAL 2 PROSES) ---
def TampilData(N, Kode, Nama, Jenis, Stok):
    # I.S. Data terdefinisi
    # F.S. Menampilkan tabel data dan statistik total (2 Proses)
    BersihkanLayar()
    print(f"{'NO':<3} | {'KODE':<10} | {'NAMA BARANG':<20} | {'JENIS':<20} | {'STOK':<5}")
    print("-" * 70)
    
    TotalBarang = 0 # Variabel untuk Proses 2 (Statistik)
    
    # Proses 1: Menampilkan Data satu per satu
    for i in range(N):
        print(f"{i+1:<3} | {Kode[i]:<10} | {Nama[i]:<20} | {Jenis[i]:<20} | {Stok[i]:<5}")
        TotalBarang += Stok[i] # Akumulasi Stok
        
    print("-" * 70)
    # Proses 2: Menampilkan Hasil Agregasi
    print(f"Total Item Unik : {N}")
    print(f"Total Fisik Stok: {TotalBarang}")
    os.system('pause')

# --- 3. PENGHAPUSAN (DELETION) ---
def HapusData(N, Kode, Nama, Jenis, Stok):
    # I.S. N dan Array terdefinisi
    # F.S. Data berkurang satu jika ditemukan, elemen bergeser
    BersihkanLayar()
    print("=== HAPUS DATA BARANG ===")
    Cari = input("Masukkan Kode Barang yang akan dihapus: ")
    
    IndexTemu = -1
    # Langkah 1: Cari Index (Sequential Search)
    for i in range(N):
        if Kode[i] == Cari:
            IndexTemu = i
            break
    
    if IndexTemu != -1:
        print(f"Data ditemukan: {Nama[IndexTemu]}")
        Yakin = input("Yakin hapus? (y/n): ")
        if Yakin.lower() == 'y':
            # Langkah 2: Geser Data (Shift Left)
            for i in range(IndexTemu, N-1):
                Kode[i] = Kode[i+1]
                Nama[i] = Nama[i+1]
                Jenis[i] = Jenis[i+1]
                Stok[i] = Stok[i+1]
            N -= 1
            print("Data berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")
    
    os.system('pause')
    return N

# --- 4. PENGURUTAN (SORTING) ---
# Menggunakan acuan Pertemuan 14

def BubbleSortKode(N, Kode, Nama, Jenis, Stok, Ascending=True):
    # Algoritma Bubble Sort untuk Kode (String)
    # Jika Ascending=True (A-Z), jika False (Z-A)
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if Ascending:
                Kondisi = Kode[j] < Kode[j-1]
            else:
                Kondisi = Kode[j] > Kode[j-1]
            
            if Kondisi:
                TukarData(j, j-1, Kode, Nama, Jenis, Stok)
    print("Pengurutan Bubble Sort Selesai.")

def SelectionSortStok(N, Kode, Nama, Jenis, Stok, Ascending=True):
    # Algoritma Selection Sort untuk Stok (Integer)
    # Mencari Min/Max lalu tukar
    for i in range(N-1):
        IndexPilih = i
        for j in range(i+1, N):
            if Ascending:
                # Cari Minimum (Ascending)
                if Stok[j] < Stok[IndexPilih]:
                    IndexPilih = j
            else:
                # Cari Maximum (Descending)
                if Stok[j] > Stok[IndexPilih]:
                    IndexPilih = j
        
        # Tukar data i dengan data terpilih (Min/Max)
        if IndexPilih != i:
            TukarData(i, IndexPilih, Kode, Nama, Jenis, Stok)
    print("Pengurutan Selection Sort Selesai.")

# --- 5. PENCARIAN (SEARCHING) ---
def MenuPencarian(N, Kode, Nama, Jenis, Stok):
    BersihkanLayar()
    print("=== MENU PENCARIAN ===")
    print("1. Cari Kode (Data Unik)")
    print("2. Cari Nama (Data Tidak Unik)")
    Pil = int(input("Pilih: "))
    
    if Pil == 1:
        Cari = input("Kode yang dicari: ")
        Ketemu = False
        for i in range(N):
            if Kode[i] == Cari:
                print(f"DITEMUKAN Index[{i}]: {Nama[i]} | Stok: {Stok[i]}")
                Ketemu = True
                break # Data unik, langsung berhenti
        if not Ketemu: print("Data tidak ditemukan.")
        
    elif Pil == 2:
        Cari = input("Nama yang dicari (bisa sebagian): ")
        print("Hasil Pencarian:")
        for i in range(N):
            # Pencarian substring (tidak harus persis sama)
            if Cari in Nama[i]:
                print(f"- {Kode[i]} | {Nama[i]} | {Jenis[i]}")
                Ketemu = True
        if not Ketemu: print("Data tidak ditemukan.")
        
    os.system('pause')

# --- PROGRAM UTAMA ---
# Deklarasi Array (Penciptaan)
KodeBrg = ["/"] * MAKS
NamaBrg = ["/"] * MAKS
JenisBrg = ["/"] * MAKS
StokBrg = [0] * MAKS
N = 0 # Jumlah data awal

Pilih = -1
while Pilih != 0:
    BersihkanLayar()
    print("=== PROGRAM GUDANG TERSTRUKTUR ===")
    print("1. Tambah Data Barang")
    print("2. Tampil Data Barang (Traversal)")
    print("3. Hapus Data Barang")
    print("4. Urutkan Kode (Bubble Sort)")
    print("5. Urutkan Stok (Selection Sort)")
    print("6. Cari Data")
    print("0. Keluar")
    
    try:
        Pilih = int(input("Pilih Menu: "))
    except:
        Pilih = -1

    if Pilih == 1:
        N = TambahData(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
    elif Pilih == 2:
        if N > 0: TampilData(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
        else: print("Data Kosong!"); os.system('pause')
    elif Pilih == 3:
        if N > 0: N = HapusData(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
        else: print("Data Kosong!"); os.system('pause')
    elif Pilih == 4:
        if N > 0:
            print("1. Ascending (A-Z)\n2. Descending (Z-A)")
            Arah = int(input("Pilih: "))
            BubbleSortKode(N, KodeBrg, NamaBrg, JenisBrg, StokBrg, Arah==1)
            TampilData(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
    elif Pilih == 5:
        if N > 0:
            print("1. Ascending (Kecil-Besar)\n2. Descending (Besar-Kecil)")
            Arah = int(input("Pilih: "))
            SelectionSortStok(N, KodeBrg, NamaBrg, JenisBrg, StokBrg, Arah==1)
            TampilData(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)
    elif Pilih == 6:
        if N > 0: MenuPencarian(N, KodeBrg, NamaBrg, JenisBrg, StokBrg)