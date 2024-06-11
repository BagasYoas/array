#
def input_data_barang():
    barang_list = []
    n = int(input("Masukkan jumlah data barang: "))

    for i in range(n):
        print(f"Memasukkan data barang ke-{i+1} :")
        nama_barang = input("Nama Barang: ")
        kode_barang = input("Kode Barang: ")
        jumlah_barang = int(input("Jumlah Barang: "))
        barang = {
            "nama" : nama_barang,
            "kode" : kode_barang,
            "jumlah" : jumlah_barang
        }
        barang_list.append(barang)
    return barang_list

#
def tampilkan_data_barang(barang_list):
    for i, brg in enumerate(barang_list):
        print( )
        print(f"Barang ke-{i+1}:")
        print(f"Nama Barang : {brg['nama']}")
        print(f"Kode Barang : {brg['kode']}")
        print(f"Jumlah Barang : {brg['jumlah']}")

#
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

#
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

# Main program
barang_list = input_data_barang()
tampilkan_data_barang(barang_list)

while True:
    print("\nMenu:")
    print("1. Tampilkan semua data barang")
    print("2. Mencari barang berdasarkan kode")
    print("3. Hapus barang berdasarkan kode")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        tampilkan_data_barang(barang_list)
    elif pilihan == '2':
        mencari_barang(barang_list)
    elif pilihan == '3':
        hapus_barang(barang_list)
    elif pilihan == '4':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")