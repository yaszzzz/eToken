class Order:
    def __init__(self, order_id, user, item, quantity):
        self.order_id = order_id
        self.user = user
        self.item = item 
        self.quantity = quantity
        self.total_price = self.calculate_total()

    def calculate_total(self):
        return self.item.price * self.quantity

    def display_order_summary(self):
       # Periksa tipe item dan tampilkan atribut yang sesuai
        item_info = ""
        if hasattr(self.item, "provider") and hasattr(self.item, "value"):
            # Jika item adalah Voucher
            item_info = f"Voucher: {self.item.provider} - {self.item.value}"
        elif hasattr(self.item, "game") and hasattr(self.item, "package"):
            # Jika item adalah TopUpGame
            item_info = f"Game: {self.item.game} - {self.item.package}"
        elif hasattr(self.item, "value"):
            # Jika item adalah Token PLN
            item_info = f"Token PLN: {self.item.value}"
        else:
            item_info = f"Item: {self.item.__class__.__name__}"

        return (f"Order ID: {self.order_id}\n"
                f"User: {self.user.name}\n"
                f"{item_info} x{self.quantity}\n"
                f"Total Price: Rp{self.total_price}")