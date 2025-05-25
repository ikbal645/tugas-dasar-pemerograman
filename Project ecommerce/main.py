from ecommerce.pricing import hitung_diskon, hitung_pajak, hitung_total
from ecommerce.order import generate_order_id

def format_rupiah(angka):
    return f"Rp {angka:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def main():
    try:
        nama_pelanggan = input("Masukkan nama pelanggan: ")
        nama_produk = input("Masukkan nama produk: ")
        harga_asli = float(input("Masukkan harga asli: "))
        persentase_diskon = float(input("Masukkan persentase diskon: "))
        persentase_pajak = float(input("Masukkan persentase pajak: "))

        harga_setelah_diskon = hitung_diskon(harga_asli, persentase_diskon)
        diskon = harga_asli - harga_setelah_diskon
        pajak = hitung_pajak(harga_setelah_diskon, persentase_pajak)
        total = hitung_total(harga_asli, persentase_diskon, persentase_pajak)
        order_id = generate_order_id()

        print("=" * 40)
        print(" " * 10 + "RINCIAN PEMBELIAN")
        print("=" * 40)
        print(f"{'ID Pesanan':20}: {order_id}")
        print(f"{'Nama Pelanggan':20}: {nama_pelanggan}")
        print(f"{'Nama Produk':20}: {nama_produk}")
        print(f"{'Harga Asli':20}: {format_rupiah(harga_asli)}")
        print(f"{'Diskon':20}: {format_rupiah(diskon)}")
        print(f"{'Pajak':20}: {format_rupiah(pajak)}")
        print(f"{'Total Belanja':20}: {format_rupiah(total)}")
        print("=" * 40)

    except ValueError:
        print("Input tidak valid. Pastikan Anda memasukkan angka untuk harga, diskon, dan pajak.")

if __name__ == "__main__":
    main()
