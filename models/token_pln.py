class TokenPLN:
    def __init__(self, token_id, denomination, price):
        self.token_id = token_id
        self.denomination = denomination
        self.price = price

    def display_token_info(self):
        return (
            f"ID Token: {self.token_id}\n"
            f"Denominasi: {self.denomination}\n"
            f"Harga: Rp{self.price:,}\n"
        )