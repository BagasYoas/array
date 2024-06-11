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
while True:
    print("\nPilih opsi:")
    print("1. Tambah Transaksi")
    print("2. Tampilkan Semua Transaksi")
    print("3. Total Pemasukan")
    print("4. Total Pengeluaran")
    print("5. Saldo Akhir")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")

    if pilihan == '1':
        tambah_transaksi()
    elif pilihan == '2':
        tampilkan_transaksi()
    elif pilihan == '3':
        total_pemasukan()
    elif pilihan == '4':
        total_pengeluaran()
    elif pilihan == '5':
        saldo_akhir()
    elif pilihan == '6':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
