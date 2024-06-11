# Fungsi untuk input data mahasiswa
def input_data_mahasiswa():
    mahasiswa_list = []
    n = int(input("Masukkan jumlah mahasiswa: "))

    for i in range(n):
        print(f"Masukkan data Mahasiswa ke-{i+1} :")
        nama = input("Nama: ")
        nim = input("NIM: ")
        nilai_absen = float(input("Nilai absen: "))
        nilai_tugas = float(input("Nilai Tugas: "))
        nilai_uts = float(input("Nilai UTS: "))
        nilai_uas = float(input("Nilai UAS: "))
        mahasiswa = {
            "nama": nama,
            "nim": nim,
            "nilai_absen": nilai_absen,
            "nilai_tugas": nilai_tugas,
            "nilai_uts": nilai_uts,
            "nilai_uas": nilai_uas,
            "rata_rata": (nilai_absen + nilai_tugas + nilai_uts + nilai_uas) / 4
        }
        mahasiswa_list.append(mahasiswa)
    return mahasiswa_list

# Fungsi untuk menampilkan data mahasiswa
def tampilkan_data_mahasiswa(mahasiswa_list):
    for i, mhs in enumerate(mahasiswa_list):
        print(f"\nMahasiswa ke-{i+1}:")
        print(f"Nama : {mhs['nama']}")
        print(f"NIM : {mhs['nim']}")
        print(f"Nilai absen : {mhs['nilai_absen']}")
        print(f"Nilai tugas : {mhs['nilai_tugas']}")
        print(f"Nilai UTS : {mhs['nilai_uts']}")
        print(f"Nilai UAS : {mhs['nilai_uas']}")
        print(f"Rata-rata : {mhs['rata_rata']}")

# Fungsi untuk menampilkan rata-rata nilai mahasiswa
def tampilkan_rata2_nilai_mahasiswa(mahasiswa_list):
    print("\nRata-rata nilai tiap mahasiswa:")
    for i, mhs in enumerate(mahasiswa_list):
        print(f"Mahasiswa ke-{i+1} ({mhs['nama']}): {mhs['rata_rata']}")

# Fungsi untuk mencari nilai tertinggi dan terendah
def cari_nilai_tertinggi_terendah(mahasiswa_list):
    nilai_tertinggi = max(mahasiswa_list, key=lambda mhs: mhs['rata_rata'])
    nilai_terendah = min(mahasiswa_list, key=lambda mhs: mhs['rata_rata'])

    print(f"\nMahasiswa dengan nilai tertinggi:")
    print(f"Nama : {nilai_tertinggi['nama']}")
    print(f"NIM : {nilai_tertinggi['nim']}")
    print(f"Rata-rata : {nilai_tertinggi['rata_rata']}")

    print(f"\nMahasiswa dengan nilai terendah:")
    print(f"Nama : {nilai_terendah['nama']}")
    print(f"NIM : {nilai_terendah['nim']}")
    print(f"Rata-rata : {nilai_terendah['rata_rata']}")

# Fungsi untuk input data barang
def input_data_barang():
    barang_list = []
    n = int(input("Masukkan jumlah data barang: "))

    for i in range(n):
        print(f"Memasukkan data barang ke-{i+1} :")
        nama_barang = input("Nama Barang: ")
        kode_barang = input("Kode Barang: ")
        jumlah_barang = int(input("Jumlah Barang: "))
        barang = {
            "nama": nama_barang,
            "kode": kode_barang,
            "jumlah": jumlah_barang
        }
        barang_list.append(barang)
    return barang_list

# Fungsi untuk menampilkan data barang
def tampilkan_data_barang(barang_list):
    for i, brg in enumerate(barang_list):
        print(f"\nBarang ke-{i+1}:")
        print(f"Nama Barang : {brg['nama']}")
        print(f"Kode Barang : {brg['kode']}")
        print(f"Jumlah Barang : {brg['jumlah']}")

# Fungsi untuk mencari barang
def mencari_barang(barang_list):
    kode = input("Masukkan kode barang yang dicari: ")
    found = False
    for brg in barang_list:
        if brg['kode'] == kode:
            print("\nBarang ditemukan:")
            print(f"Nama Barang : {brg['nama']}")
            print(f"Kode Barang : {brg['kode']}")
            print(f"Jumlah Barang : {brg['jumlah']}")
            found = True
            break
    if not found:
        print("\nBarang dengan kode tersebut tidak ditemukan.")

# Fungsi untuk menghapus barang
def hapus_barang(barang_list):
    kode = input("Masukkan kode barang yang ingin dihapus: ")
    found = False
    for i, brg in enumerate(barang_list):
        if brg['kode'] == kode:
            print(f"\nMenghapus barang dengan kode {kode}:")
            print(f"Nama Barang : {brg['nama']}")
            print(f"Kode Barang : {brg['kode']}")
            print(f"Jumlah Barang : {brg['jumlah']}")
            del barang_list[i]
            found = True
            print("\nBarang berhasil dihapus.")
            break
    if not found:
        print("\nBarang dengan kode tersebut tidak ditemukan.")

# Daftar untuk menyimpan transaksi
transaksi = []

# Fungsi untuk menginput dan menambahkan transaksi
def tambah_transaksi():
    tipe = input("Masukkan tipe transaksi (pemasukan/pengeluaran): ").lower()
    if tipe not in ['pemasukan', 'pengeluaran']:
        print("Tipe transaksi tidak valid!")
        return
    
    try:
        jumlah = float(input("Masukkan jumlah transaksi: "))
        transaksi.append({"tipe": tipe, "jumlah": jumlah})
        print("Transaksi berhasil ditambahkan!")
    except ValueError:
        print("Jumlah tidak valid! Harus berupa angka.")

# Fungsi untuk menampilkan semua transaksi
def tampilkan_transaksi():
    if not transaksi:
        print("Tidak ada transaksi.")
    else:
        for t in transaksi:
            print(f"Tipe: {t['tipe']}, Jumlah: {t['jumlah']}")

# Fungsi untuk menghitung dan menampilkan total pemasukan
def total_pemasukan():
    total = sum(t['jumlah'] for t in transaksi if t['tipe'] == 'pemasukan')
    print(f"Total Pemasukan: {total}")
    return total

# Fungsi untuk menghitung dan menampilkan total pengeluaran
def total_pengeluaran():
    total = sum(t['jumlah'] for t in transaksi if t['tipe'] == 'pengeluaran')
    print(f"Total Pengeluaran: {total}")
    return total

# Fungsi untuk menghitung dan menampilkan saldo akhir
def saldo_akhir():
    pemasukan = total_pemasukan()
    pengeluaran = total_pengeluaran()
    saldo = pemasukan - pengeluaran
    print(f"Saldo Akhir: {saldo}")
    return saldo

# Fungsi utama untuk menjalankan program
def main():
    mahasiswa_list = []
    barang_list = []
    
    while True:
        print("\nMenu Utama:")
        print("1. Kelola Data Mahasiswa")
        print("2. Kelola Data Barang")
        print("3. Kelola Transaksi Keuangan")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            while True:
                print("\nMenu Data Mahasiswa:")
                print("1. Input Data Mahasiswa")
                print("2. Tampilkan Data Mahasiswa")
                print("3. Tampilkan Rata-rata Nilai Mahasiswa")
                print("4. Cari Nilai Tertinggi dan Terendah")
                print("5. Kembali ke Menu Utama")
                
                sub_pilihan = input("Pilih menu (1/2/3/4/5): ")

                if sub_pilihan == '1':
                    mahasiswa_list = input_data_mahasiswa()
                elif sub_pilihan == '2':
                    tampilkan_data_mahasiswa(mahasiswa_list)
                elif sub_pilihan == '3':
                    tampilkan_rata2_nilai_mahasiswa(mahasiswa_list)
                elif sub_pilihan == '4':
                    cari_nilai_tertinggi_terendah(mahasiswa_list)
                elif sub_pilihan == '5':
                    break
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")
        
        elif pilihan == '2':
            while True:
                print("\nMenu Data Barang:")
                print("1. Input Data Barang")
                print("2. Tampilkan Data Barang")
                print("3. Mencari Barang Berdasarkan Kode")
                print("4. Hapus Barang Berdasarkan Kode")
                print("5. Kembali ke Menu Utama")
                
                sub_pilihan = input("Pilih menu (1/2/3/4/5): ")

                if sub_pilihan == '1':
                    barang_list = input_data_barang()
                elif sub_pilihan == '2':
                    tampilkan_data_barang(barang_list)
                elif sub_pilihan == '3':
                    mencari_barang(barang_list)
                elif sub_pilihan == '4':
                    hapus_barang(barang_list)
                elif sub_pilihan == '5':
                    break
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")
        
        elif pilihan == '3':
            while True:
                print("\nMenu Transaksi Keuangan:")
                print("1. Tambah Transaksi")
                print("2. Tampilkan Semua Transaksi")
                print("3. Total Pemasukan")
                print("4. Total Pengeluaran")
                print("5. Saldo Akhir")
                print("6. Kembali ke Menu Utama")
                
                sub_pilihan = input("Pilih menu (1/2/3/4/5/6): ")

                if sub_pilihan == '1':
                    tambah_transaksi()
                elif sub_pilihan == '2':
                    tampilkan_transaksi()
                elif sub_pilihan == '3':
                    total_pemasukan()
                elif sub_pilihan == '4':
                    total_pengeluaran()
                elif sub_pilihan == '5':
                    saldo_akhir()
                elif sub_pilihan == '6':
                    break
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")
        
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini.")
            break
        
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()
