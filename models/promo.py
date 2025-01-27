class Promo:
    def __init__(self, code, discount_percentage):
        self.code = code
        self.discount_percentage = discount_percentage

    def apply_discount(self, total_price):
        return total_price - (total_price * self.discount_percentage / 100)
