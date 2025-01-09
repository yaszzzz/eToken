import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TransactionManager:
    def __init__(self):
        self.orders = []  # List untuk menyimpan semua pesanan

    def create_order(self, order_id, user, voucher, quantity):
        from models.order import Order
        order = Order(order_id, user, voucher, quantity)
        self.orders.append(order)
        return order

    def display_all_orders(self):
        if not self.orders:
            return "No orders have been made yet."
        return "\n\n".join([order.display_order_summary() for order in self.orders])