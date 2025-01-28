``python
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Menu:
    def __init__(self):
        self.choices = {
            "1": self.create_user,
            "2": self.change_active_user,
            "3": self.create_order,
            "4": self.display_all_orders,
            "5": self.display_active_user_info,
            "6": self.apply_promo_code,
            "7": self.exit_program
        }

    def display_menu(self):
        print("\n=== Menu ===")
        print("1. Buat Pengguna Baru")
        print("2. Ganti Pengguna Aktif")
        print("3. Buat Pesanan Baru")
        print("4. Tampilkan Semua Pesanan")
        print("5. Tampilkan Informasi Pengguna Aktif")
        print("6. Gunakan Kode Promo")
        print("7. Keluar")

    def create_user(self, users):
        print("\n=== Buat Pengguna Baru ===")
        name = input("Masukkan nama: ")
        email = input("Masukkan email: ")
        phone_number = input("Masukkan nomor telepon: ")
        user_id = len(users) + 1
        new_user = User(user_id, name, email, phone_number)
        users.append(new_user)
        print(f"Pengguna baru '{name}' berhasil dibuat!")

    def change_active_user(self, users, active_user):
        print("\n=== Ganti Pengguna Aktif ===")
        if not users:
            print("Belum ada pengguna yang dibuat.")
            return
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

    def create_order(self, active_user, voucher1, voucher2, voucher3, transaction_manager):
        if not active_user:
            print("Silakan pilih pengguna aktif terlebih dahulu.")
            return
        print("\n=== Buat Pesanan Baru ===")
        print("Voucher yang tersedia:")
        print(f"1. {voucher1.display_voucher_info()}")
        print(f"2. {voucher2.display_voucher_info()}")
        print(f"3. {voucher3.display_voucher_info()}")
        
        voucher_choice = input("Pilih voucher (1-3): ")
        if voucher_choice ==e True:
        print("\n=== Menu ===")
        print("1. Buat Pengguna Baru")
        print("2. Ganti Pengguna Aktif")
        print("3. Buat Pesanan Baru")
        print("4. Tampilkan Semua Pesanan")
        print("5. Tampilkan Informasi Pengguna Aktif")
        print("6. Gunakan Kode Promo")
        print("7. Keluar")

        choice = input("Pilih opsi (1-7): ")

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
                order_id = len(transaction_manager.orders) + 1
                transaction_manager.create_order(order_id, active_user, selected_voucher, quantity)
                print(f"Pesanan dengan Order Id {order_id} berhasil dibuat!")

            except ValueError:
                print("Jumlah harus berupa angka.")


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
            print("\n=== Gunakan Kode Promo ===")
            if not transaction_manager.orders:
                print("Belum ada pesanan yang dibuat.")
                continue

            order_id = input("Masukkan Order ID: ")
            try:
                order_id = int(order_id)
            except ValueError:
                print("Order ID harus berupa angka.")
                continue

            # Cari pesanan berdasarkan Order ID
            selected_order = None
            for order in transaction_manager.orders:
                if order.order_id == order_id:
                    selected_order = order
                    break

            if not selected_order:
                print("Order ID tidak ditemukan.")
                continue

            promo_code = input("Masukkan kode promo: ").strip()

            # Terapkan diskon jika kode valid
            if promo_code in transaction_manager.promos:
                promo = transaction_manager.promos[promo_code]
                selected_order.total_price = promo.apply_discount(selected_order.total_price)
                print(f"Kode promo '{promo_code}' diterapkan! Total harga setelah diskon: {selected_order.total_price}")
            else:
                print("Kode promo tidak valid atau sudah kadaluarsa.")
        elif choice == "7":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
