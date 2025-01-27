import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    from models.user import User
    from models.voucher import Voucher
    from models.transaction_manager import TransactionManager

    # Daftar pengguna dan objek pengguna aktif
    users = []
    active_user = None

    # Membuat objek Voucher
    voucher1 = Voucher(101, "Telkomsel", "100.000", 95000)
    voucher2 = Voucher(102, "Indosat", "50.000", 48000)
    voucher3 = Voucher(103, "XL", "60.000", 58000)

    # Membuat objek TransactionManager
    transaction_manager = TransactionManager()

    while True:
        print("\n=== Menu ===")
        print("1. Buat Pengguna Baru")
        print("2. Ganti Pengguna Aktif")
        print("3. Buat Pesanan Baru")
        print("4. Tampilkan Semua Pesanan")
        print("5. Tampilkan Informasi Pengguna Aktif")
        print("6. Keluar")
        choice = input("Pilih opsi (1-6): ")

        if choice == "1":
            print("\n=== Buat Pengguna Baru ===")
            name = input("Masukkan nama: ")
            email = input("Masukkan email: ")
            phone_number = input("Masukkan nomor telepon: ")
            user_id = len(users) + 1
            new_user = User(user_id, name, email, phone_number)
            users.append(new_user)
            print(f"Pengguna baru '{name}' berhasil dibuat!")
        elif choice == "2":
            print("\n=== Ganti Pengguna Aktif ===")
            if not users:
                print("Belum ada pengguna yang dibuat.")
                continue
            print("Daftar Pengguna:")
            for idx, user in enumerate(users):
                print(f"{idx + 1}. {user.display_user_info()}")
            user_choice = input("Pilih pengguna (nomor): ")
            try:
                user_choice = int(user_choice)
                if 1 <= user_choice <= len(users):
                    active_user = users[user_choice - 1]
                    print(f"Pengguna aktif sekarang: {active_user.name}")
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Masukkan nomor yang valid.")
        elif choice == "3":
            if not active_user:
                print("Silakan pilih pengguna aktif terlebih dahulu.")
                continue
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
            except ValueError:
                print("Jumlah harus berupa angka.")
                continue

            promo_code = input("Masukkan kode promo (jika ada, tekan Enter untuk lanjut): ").strip()

            order_id = len(transaction_manager.orders) + 1
            transaction_manager.create_order(order_id, active_user, selected_voucher, quantity, promo_code)

            print("Pesanan berhasil dibuat!")


        elif choice == "4":
            print("\n=== Semua Pesanan ===")
            print(transaction_manager.display_all_orders())
        elif choice == "5":
            if not active_user:
                print("Belum ada pengguna aktif.")
            else:
                print("\n=== Informasi Pengguna Aktif ===")
                print(active_user.display_user_info())
        elif choice == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
