# ecommerce/order.py
from datetime import datetime
import random

def generate_order_id():
    """Menghasilkan ID pesanan unik dengan tanggal."""
    tanggal = datetime.now().strftime("%Y%m%d")
    random_number = random.randint(100000, 999999)
    return f"ORDER-{tanggal}-{random_number}"
