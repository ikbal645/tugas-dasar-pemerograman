# ecommerce/pricing.py
def hitung_diskon(harga, persentase_diskon):
    """Menghitung harga setelah diskon."""
    diskon = harga * (persentase_diskon / 100)
    return max(harga - diskon, 0)  # Menghindari nilai negatif

def hitung_pajak(harga, persentase_pajak):
    """Menghitung pajak dari harga."""
    return harga * (persentase_pajak / 100)

def hitung_total(harga, persentase_diskon, persentase_pajak):
    """Menghitung total belanja setelah diskon dan pajak."""
    harga_setelah_diskon = hitung_diskon(harga, persentase_diskon)
    pajak = hitung_pajak(harga_setelah_diskon, persentase_pajak)
    return harga_setelah_diskon + pajak
