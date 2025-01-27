import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TransactionManager:
    def __init__(self):
        from models.promo import Promo
        self.orders = [] 
        self.promos = {
            "DISKON10": Promo("DISKON10", 10),
            "DISKON20": Promo("DISKON20", 20)
        }

    def create_order(self, order_id, user, voucher, quantity, promo_code=None):
        from models.order import Order
        order = Order(order_id, user, voucher, quantity)

        if promo_code and promo_code in self.promos:
            promo = self.promos[promo_code]
            order.total_price = promo.apply_discount(order.total_price)
            print(f"Kode promo '{promo_code}' diterapkan! Total harga setelah diskon: {order.total_price}")
        else:
            if promo_code:
                print("Kode promo tidak valid atau sudah kadaluarsa.")

        self.orders.append(order)
        return order

    def display_all_orders(self):
        if not self.orders:
            return "No orders have been made yet."
        return "\n\n".join([order.display_order_summary() for order in self.orders])