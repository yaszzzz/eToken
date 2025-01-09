
class Voucher:
    def __init__(self, voucher_id, provider, value, price):
        self.voucher_id = voucher_id
        self.provider = provider
        self.value = value
        self.price = price

    def display_voucher_info(self):
        return f"Voucher ID: {self.voucher_id}, Provider: {self.provider}, Value: {self.value}, Price: {self.price}"