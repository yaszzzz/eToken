import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    from models.user import User
    from models.voucher import Voucher
    from models.transaction_manager import TransactionManager
    
    # Membuat objek User
    user1 = User(1, "Aditya Putra", "aditya@example.com")

    # Membuat objek Voucher
    voucher1 = Voucher(101, "Telkomsel", "100.000", 95000)
    voucher2 = Voucher(102, "Indosat", "50.000", 48000)

    # Membuat objek TransactionManager
    transaction_manager = TransactionManager()

    # Membuat pesanan melalui TransactionManager
    order1 = transaction_manager.create_order(5001, user1, voucher1, 2)
    order2 = transaction_manager.create_order(5002, user1, voucher2, 3)

    # Menampilkan semua pesanan
    print(transaction_manager.display_all_orders())

if __name__ == "__main__":
    main()
