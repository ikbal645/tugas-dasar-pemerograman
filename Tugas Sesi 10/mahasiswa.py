data_mahasiswa = {}

def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")
    ipk = float(input("Masukkan IPK: "))
    data_mahasiswa[nim] = {"Nama": nama, "Jurusan": jurusan, "IPK": ipk}

def tampilkan_semua():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        for nim, info in data_mahasiswa.items():
            print(f"NIM: {nim}, Nama: {info['Nama']}, Jurusan: {info['Jurusan']}, IPK: {info['IPK']}")

def cari_mahasiswa():
    nim = input("Masukkan NIM yang dicari: ")
    if nim in data_mahasiswa:
        info = data_mahasiswa[nim]
        print(f"Nama: {info['Nama']}, Jurusan: {info['Jurusan']}, IPK: {info['IPK']}")
    else:
        print("Mahasiswa tidak ditemukan.")

def hapus_mahasiswa():
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus.")
    else:
        print("Mahasiswa tidak ditemukan.")

# Menu interaktif
while True:
    print("\n1. Tambah Mahasiswa")
    print("2. Tampilkan Semua")
    print("3. Cari Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")
    pilihan = input("Pilih opsi (1-5): ")
    
    if pilihan == '1':
        tambah_mahasiswa()
    elif pilihan == '2':
        tampilkan_semua()
    elif pilihan == '3':
        cari_mahasiswa()
    elif pilihan == '4':
        hapus_mahasiswa()
    elif pilihan == '5':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")