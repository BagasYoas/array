# buat fungsi untuk menginput data mahasiswa
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
            "nama" : nama,
            "nim" : nim,
            "nilai_absen" : nilai_absen,
            "nilai_tugas" : nilai_tugas,
            "nilai_uts" : nilai_uts,
            "nilai_uas" : nilai_uas,
            "rata_rata" : (nilai_absen + nilai_tugas + nilai_uts + nilai_uas) / 4
        }
        mahasiswa_list.append(mahasiswa)
    return mahasiswa_list

#buat fungsi untuk menampilkan data mahasiswa
def tampilkan_data_mahasiswa(mahasiswa_list):
    for i, mhs in enumerate(mahasiswa_list):
        print( )
        print(f"Mahasiswa ke-{i+1}:")
        print(f"Nama : {mhs['nama']}")
        print(f"NIM : {mhs['nim']}")
        print(f"Nilai absen : {mhs['nilai_absen']}")
        print(f"Nilai tugas : {mhs['nilai_tugas']}")
        print(f"Nilai UTS : {mhs['nilai_uts']}")
        print(f"Nilai UAS : {mhs['nilai_uas']}")
        print(f"Rata-rata : {mhs['rata_rata']}")

#buat fungsi untuk menghitung dan menampilkan rata-rata nilai mahasiswa
def tampilkan_rata2_nilai_mahasiswa(mahasiswa_list):
    print("\nRata-rata nilai tiap mahasiswa:")
    for i, mhs in enumerate(mahasiswa_list):
        print(f"Mahasiswa ke-{i+1} ({mhs['nama']}): {mhs['rata_rata']}")

#buat fungsi untuk mencari dan menampilkan mahasiswa dengan nilai tertinggi dan terendah
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

# Main program
mahasiswa_list = input_data_mahasiswa()
tampilkan_data_mahasiswa(mahasiswa_list)
tampilkan_rata2_nilai_mahasiswa(mahasiswa_list)
cari_nilai_tertinggi_terendah(mahasiswa_list)
