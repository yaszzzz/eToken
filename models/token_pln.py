# punya ilyas 

import random
from datetime import datetime

class TokenPLN:
    # Menyimpan semua riwayat pemesanan
    order_history = []
    
    def __init__(self, token_id, denomination, price):
        self.token_id = token_id
        self.denomination = denomination
        self.price = price
        self.created_at = datetime.now()
        
    def display_token_info(self):
        return (
            f"ID Token: {self.token_id}\n"
            f"Denominasi: {self.denomination} kWh\n"
            f"Harga: Rp{self.price:,}\n"
            f"Tanggal: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

    @staticmethod
    def generate_token_number():
        """Fungsi untuk menghasilkan nomor token PLN secara acak."""
        return ''.join([str(random.randint(0, 9)) for _ in range(12)])

    @staticmethod
    def validate_quantity(quantity):
        """Memvalidasi jumlah pembelian token."""
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Jumlah pembelian harus lebih dari 0")
            if quantity > 10:
                raise ValueError("Maksimal pembelian 10 token per transaksi")
            return quantity
        except ValueError as e:
            raise ValueError("Jumlah pembelian harus berupa angka positif")

    @staticmethod
    def create_order(selected_token, quantity, username):
        """Fungsi untuk membuat order token PLN."""
        try:
            # Validasi quantity
            validated_quantity = TokenPLN.validate_quantity(quantity)
            
            # Generate token untuk setiap pembelian
            tokens = []
            for _ in range(validated_quantity):
                token_number = TokenPLN.generate_token_number()
                tokens.append(token_number)
            
            # Hitung total harga
            total_price = selected_token.price * validated_quantity
            
            # Buat data order
            order_data = {
                'username': username,
                'order_id': selected_token.token_id,
                'denomination': selected_token.denomination,
                'quantity': validated_quantity,
                'total_price': total_price,
                'tokens': tokens,
                'timestamp': datetime.now()
            }
            
            # Simpan ke riwayat
            TokenPLN.order_history.append(order_data)
            
            # Buat struk pembelian
            print("\n" + "="*40)
            print("STRUK PEMBELIAN TOKEN LISTRIK PLN")
            print("="*40)
            print(f"Order ID: {selected_token.token_id}")
            print(f"Pelanggan: {username}")
            print(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Denominasi: {selected_token.denomination} kWh")
            print(f"Harga per token: Rp{selected_token.price:,}")
            print(f"Jumlah pembelian: {validated_quantity}")
            print(f"Total harga: Rp{total_price:,}")
            print("\nToken yang dibeli:")
            for i, token in enumerate(tokens, 1):
                print(f"{i}. {token}")
            print("="*40)
            
            return order_data
            
        except ValueError as e:
            print(f"Error: {str(e)}")
            return None

    @staticmethod
    def display_order_history(username=None):
        """Menampilkan riwayat pemesanan token."""
        filtered_history = [
            order for order in TokenPLN.order_history
            if username is None or order['username'] == username
        ]
        
        if not filtered_history:
            print("\nBelum ada riwayat pemesanan token.")
            return
        
        print("\n" + "="*50)
        print("RIWAYAT PEMESANAN TOKEN PLN")
        print("="*50)
        
        for idx, order in enumerate(filtered_history, 1):
            print(f"\nPemesanan #{idx}")
            print(f"Tanggal: {order['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Username: {order['username']}")
            print(f"Order ID: {order['order_id']}")
            print(f"Denominasi: {order['denomination']} kWh")
            print(f"Jumlah: {order['quantity']}")
            print(f"Total Harga: Rp{order['total_price']:,}")
            print(f"Token:")
            for i, token in enumerate(order['tokens'], 1):
                print(f"  {i}. {token}")
            print("-"*50)