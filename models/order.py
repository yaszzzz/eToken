class Order:
    def __init__(self, order_id, user, voucher, quantity):
        self.order_id = order_id
        self.user = user
        self.voucher = voucher
        self.quantity = quantity
        self.total_price = self.calculate_total()

    def calculate_total(self):
        return self.voucher.price * self.quantity

    def display_order_summary(self):
        return (f"Order ID: {self.order_id}\n"
                f"User: {self.user.name}\n"
                f"Voucher: {self.voucher.provider} - {self.voucher.value}\n"
                f"Quantity: {self.quantity}\n"
                f"Total Price: {self.total_price}")