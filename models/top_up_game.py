class TopUpGame:
    def __init__(self, game_id, game_name, package_name, price):
        self.game_id = game_id
        self.game_name = game_name
        self.package_name = package_name
        self.price = price

    def display_game_info(self):
        return (
            f"ID Game: {self.game_id}\n"
            f"Nama Game: {self.game_name}\n"
            f"Paket: {self.package_name}\n"
            f"Harga: Rp{self.price:,}\n"
        )