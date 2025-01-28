import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TransactionManager:
    def __init__(self):
        from models.promo import Promo
        self.orders = []  # List untuk menyimpan semua pesanan
        self.promos = {
            "DISKON10": Promo("DISKON10", 10),  # Diskon 10%
            "DISKON20": Promo("DISKON20", 20)   # Diskon 20%
        }

    def create_order(self, order_id, user, item, quantity, promo_code=None):
        from models.order import Order
        try:
            # Validasi input untuk memastikan jumlah pesanan adalah angka positif
            quantity = int(quantity)
            if quantity <= 0:
                print("Jumlah pesanan harus lebih dari 0.")
                return None

            # Membuat instance Order
            order = Order(order_id, user, item, quantity)

            # Memproses kode promo jika diberikan
            if promo_code:
                discount = self.apply_promo_code(promo_code, order)
                if discount:
                    print(f"Kode promo '{promo_code}' diterapkan! Diskon: Rp{discount}. Total harga setelah diskon: Rp{order.total_price}")
                else:
                    print("Kode promo tidak valid atau sudah kadaluarsa.")

            # Menambahkan pesanan ke daftar orders
            self.orders.append(order)
            return order
        except ValueError:
            print("Jumlah pesanan harus berupa angka valid.")
            return None
        except Exception as e:
            print(f"Terjadi error saat membuat pesanan: {e}")
            return None

    def apply_promo_code(self, promo_code, order):
        """Menerapkan kode promo pada sebuah pesanan."""
        if promo_code in self.promos:
            promo = self.promos[promo_code]
            discount = promo.apply_discount(order.total_price)  # Menghitung diskon
            order.total_price -= discount  # Mengurangi total harga dengan diskon
            return discount
        return None

   
        """
        Memproses pembayaran tagihan untuk pengguna aktif.
        """
        try:
            # Pastikan tagihan belum dibayar
            if bill["status"] == "paid":
                print("Tagihan ini sudah dibayar.")
                return False

            # Proses pembayaran
            bill["status"] = "paid"
            print(f"Pembayaran tagihan '{bill['name']}' sebesar Rp{bill['amount']} berhasil dilakukan.")
            return True
        except KeyError as e:
            print(f"Kesalahan data tagihan: {e}")
            return False
        except Exception as e:
            print(f"Terjadi kesalahan saat membayar tagihan: {e}")
            return False

    def display_all_orders(self):
        """Menampilkan semua pesanan yang telah dibuat."""
        if not self.orders:
            return "No orders have been made yet."
        try:
            # Mengumpulkan ringkasan dari semua pesanan
            order_summaries = [order.display_order_summary() for order in self.orders]
            return "\n\n".join(order_summaries)
        except AttributeError as e:
            return f"Error saat menampilkan pesanan: {e}"
        except Exception as e:
            return f"Terjadi error yang tidak terduga: {e}"
