import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    from models.user import User
    from models.voucher import Voucher
    from models.transaction_manager import TransactionManager

    user1 = User(1, "Aditya Putra", "aditya@example.com")

    voucher1 = Voucher(101, "Telkomsel", "100.000", 95000)
    voucher2 = Voucher(102, "Indosat", "50.000", 48000)
    voucher3 = Voucher(103, "XL", "60.000", 58000)

    transaction_manager = TransactionManager()

    # Menu loop
    while True:
        print("\n=== Menu ===")
        print("1. Buat Pesanan Baru")
        print("2. Tampilkan Semua Pesanan")
        print("3. Tampilkan Informasi Pengguna")
        print("4. Keluar")
        choice = input("Pilih opsi (1-4): ")

        if choice == "1":
            print("\n=== Buat Pesanan Baru ===")
            print("Voucher yang tersedia:")
            print(f"1. {voucher1.display_voucher_info()}")
            print(f"2. {voucher2.display_voucher_info()}")
            print(f"3. {voucher3.display_voucher_info()}")
            voucher_choice = input("Pilih voucher (1-3): ")
            if voucher_choice == "1":
                selected_voucher = voucher1
            elif voucher_choice == "2":
                selected_voucher = voucher2
            elif voucher_choice == "3":
                selected_voucher = voucher3
            else:
                print("Pilihan voucher tidak valid.")
                continue
            quantity = input("Masukkan jumlah: ")
            try:
                quantity = int(quantity)
                order_id = len(transaction_manager.orders) + 1  # ID otomatis
                transaction_manager.create_order(order_id, user1, selected_voucher, quantity)
                print("Pesanan berhasil dibuat!")
            except ValueError:
                print("Jumlah harus berupa angka.")
        elif choice == "2":
            print("\n=== Semua Pesanan ===")
            print(transaction_manager.display_all_orders())
        elif choice == "3":
            print("\n=== Informasi Pengguna ===")
            print(user1.display_user_info())
        elif choice == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
