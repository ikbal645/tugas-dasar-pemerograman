inventaris = {}

def tambah_barang():
    nama = input("Nama Barang: ")
    if nama in inventaris:
        print("Barang sudah ada.")
        return
    harga = float(input("Harga: "))
    stok = int(input("Stok: "))
    inventaris[nama] = (harga, stok)

def tampilkan_semua():
    if not inventaris:
        print("Inventaris kosong.")
        return
    print(f"{'Nama Barang':<20} {'Harga':<10} {'Stok':<5}")
    print("-" * 40)
    for nama, (harga, stok) in inventaris.items():
        print(f"{nama:<20} {harga:<10} {stok:<5}")

def cari_barang():
    nama = input("Masukkan nama barang yang dicari: ")
    if nama in inventaris:
        harga, stok = inventaris[nama]
        print(f"Nama: {nama}, Harga: {harga}, Stok: {stok}")
    else:
        print("Barang tidak ditemukan.")

def perbarui_stok():
    nama = input("Masukkan nama barang yang ingin diperbarui: ")
    if nama in inventaris:
        stok_baru = int(input("Masukkan stok baru: "))
        harga = inventaris[nama][0]
        inventaris[nama] = (harga, stok_baru)
        print("Stok berhasil diperbarui.")
    else:
        print("Barang tidak ditemukan.")

def hapus_barang():
    nama = input("Masukkan nama barang yang ingin dihapus: ")
    if nama in inventaris:
        del inventaris[nama]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

def analisis_data():
    if not inventaris:
        print("Inventaris kosong.")
        return
    # Barang dengan harga tertinggi dan terendah
    tertinggi = max(inventaris.items(), key=lambda item: item[1][0])
    terendah = min(inventaris.items(), key=lambda item: item[1][0])
    print(f"Barang termahal: {tertinggi[0]} (Rp {tertinggi[1][0]})")
    print(f"Barang termurah: {terendah[0]} (Rp {terendah[1][0]})")
    
    # Total nilai stok
    total_stok = sum(harga * stok for harga, stok in inventaris.values())
    print(f"Total nilai stok: Rp {total_stok}")

# Menu utama
while True:
    print("\n=== MENU INVENTARIS ===")
    print("1. Tambah Barang Baru")
    print("2. Tampilkan Semua Barang")
    print("3. Cari Barang")
    print("4. Perbarui Stok Barang")
    print("5. Hapus Barang")
    print("6. Analisis Data")
    print("7. Keluar Program")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == '1':
        tambah_barang()
    elif pilihan == '2':
        tampilkan_semua()
    elif pilihan == '3':
        cari_barang()
    elif pilihan == '4':
        perbarui_stok()
    elif pilihan == '5':
        hapus_barang()
    elif pilihan == '6':
        analisis_data()
    elif pilihan == '7':
        print("Terima kasih, program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-7.")