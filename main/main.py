import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    from models.user import User
    from models.voucher import Voucher
    from models.transaction_manager import TransactionManager
    from models.token_pln import TokenPLN
    from models.top_up_game import TopUpGame
    from models.tagihan import Tagihan

    # Data Awal
    users = []
    active_user = None

    vouchers = [
        Voucher(101, "Telkomsel", "100.000", 95000),
        Voucher(102, "Indosat", "50.000", 48000),
        Voucher(103, "XL", "60.000", 58000)
    ]

    transaction_manager = TransactionManager()

    tokens = [
        TokenPLN("TOKEN20", 20, 22000),
        TokenPLN("TOKEN50", 50, 54000),
        TokenPLN("TOKEN100", 100, 107000),
        TokenPLN("TOKEN200", 200, 212000)
    ]

    games = [
        TopUpGame(301, "Mobile Legends", "86 Diamonds", 20000),
        TopUpGame(302, "Free Fire", "70 Diamonds", 15000),
        TopUpGame(303, "PUBG Mobile", "50 UC", 25000)
    ]

    bills = [
        Tagihan(401, "BPJS", 150000, "2025-01-31"),
        Tagihan(402, "Indihome", 350000, "2025-01-30")
    ]

    def select_user():
        nonlocal active_user
        print("\n=== Ganti Pengguna Aktif ===")
        if not users:
            print("Belum ada pengguna yang dibuat.")
            return

        print("Daftar Pengguna:")
        for idx, user in enumerate(users):
            print(f"{idx + 1}. {user.display_user_info()}")
        try:
            user_choice = int(input("Pilih pengguna (nomor): "))
            if 1 <= user_choice <= len(users):
                active_user = users[user_choice - 1]
                print(f"Pengguna aktif sekarang: {active_user.name}")
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")

    def create_order(item, quantity):
        if not active_user:
            print("Silakan pilih pengguna aktif terlebih dahulu.")
            return
        try:
            quantity = int(quantity)
            order_id = len(transaction_manager.orders) + 1
            transaction_manager.create_order(order_id, active_user, item, quantity)
            print(f"Pesanan dengan Order ID {order_id} berhasil dibuat!")
        except ValueError:
            print("Jumlah harus berupa angka.")

    def display_token_menu(active_user):   #display menu token PLN punya ilyas
        while True:
            print("\n" + "="*40)
            print("=== MENU PEMBELIAN TOKEN PLN ===")
            print("="*40)
            
            if not active_user:
                print("Silakan pilih pengguna aktif terlebih dahulu.")
                return
            
            print("\nMenu:")
            print("1. Lihat Daftar Token")
            print("2. Beli Token")
            print("3. Riwayat Pemesanan")
            print("0. Kembali ke Menu Utama")
            
            menu_choice = input("\nPilih menu (0-3): ")
            
            if menu_choice == "0":
                break
                
            elif menu_choice == "1":
                # Tampilkan daftar token
                print("\nDaftar Token PLN yang Tersedia:")
                for idx, token in enumerate(tokens, start=1):
                    print(f"\nToken {idx}:")
                    print(token.display_token_info())
                input("\nTekan Enter untuk kembali ke menu...")
                
            elif menu_choice == "2":
                # Tampilkan daftar token dulu
                print("\nDaftar Token PLN yang Tersedia:")
                for idx, token in enumerate(tokens, start=1):
                    print(f"\nToken {idx}:")
                    print(token.display_token_info())
                    
                try:
                    # Pilih token
                    token_choice = int(input("\nPilih token PLN (nomor): "))
                    if token_choice < 1 or token_choice > len(tokens):
                        raise ValueError("Nomor token tidak valid")
                    
                    selected_token = tokens[token_choice - 1]
                    
                    # Input jumlah
                    quantity = input("Masukkan jumlah token yang ingin dibeli: ")
                    
                    # Proses pembelian
                    order = TokenPLN.create_order(selected_token, quantity, active_user.name)
                    
                    if order:
                        # Tambahkan ke riwayat pemesanan
                        if not hasattr(active_user, 'token_history'):
                            active_user.token_history = []
                        active_user.token_history.append(order)
                        input("\nTekan Enter untuk kembali ke menu...")
                    
                except ValueError as e:
                    print(f"\nError: {str(e)}")
                    input("\nTekan Enter untuk mencoba lagi...")
                except IndexError:
                    print("\nError: Pilihan token tidak valid")
                    input("\nTekan Enter untuk mencoba lagi...")
                    
            elif menu_choice == "3":
                # Tampilkan riwayat pemesanan
                if not hasattr(active_user, 'token_history') or not active_user.token_history:
                    print("\nBelum ada riwayat pemesanan token.")
                else:
                    print("\n" + "="*50)
                    print("RIWAYAT PEMESANAN TOKEN PLN")
                    print("="*50)
                    
                    for idx, order in enumerate(active_user.token_history, 1):
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
                        
                input("\nTekan Enter untuk kembali ke menu...")
                
            else:
                print("\nPilihan menu tidak valid")
                input("Tekan Enter untuk mencoba lagi...")
    
    def display_menu():
        print("\n=== Menu ===")
        print("1. Buat Pengguna Baru")
        print("2. Ganti Pengguna Aktif")
        print("3. Buat Pesanan Voucher")
        print("4. Tampilkan Semua Pesanan")
        print("5. Tampilkan Informasi Pengguna Aktif")
        print("6. Gunakan Kode Promo")
        print("7. Token PLN")
        print("8. Top-Up Game")
        print("9. Bayar Tagihan")
        print("10. Keluar")

    while True:
        display_menu()
        choice = input("Pilih opsi (1-10): ").strip()

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
            select_user()

        elif choice == "3":
            if not active_user:
                print("Silakan pilih pengguna aktif terlebih dahulu.")
                continue
            print("\n=== Buat Pesanan Voucher ===")
            for idx, voucher in enumerate(vouchers, start=1):
                print(f"{idx}. {voucher.display_voucher_info()}")
            try:
                voucher_choice = int(input("Pilih voucher (1-3): "))
                selected_voucher = vouchers[voucher_choice - 1]
                quantity = input("Masukkan jumlah: ")
                create_order(selected_voucher, quantity)
            except (IndexError, ValueError):
                print("Pilihan voucher tidak valid.")

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
            if not active_user:
                print("Silakan pilih pengguna aktif terlebih dahulu.")
                continue

            if not transaction_manager.orders:
                print("Tidak ada pesanan untuk pengguna ini. Silakan buat pesanan terlebih dahulu.")
                continue

            user_orders = [order for order in transaction_manager.orders if order.user == active_user]
            if not user_orders:
                print("Tidak ada pesanan yang terkait dengan pengguna aktif.")
                continue

            last_order = user_orders[-1]
            promo_code = input("Masukkan kode promo: ").strip()
            discount = transaction_manager.apply_promo_code(promo_code, last_order)

            if discount:
                print(f"Kode promo berhasil digunakan! Anda mendapatkan diskon Rp{discount}.")
                print(f"Total harga setelah diskon: Rp{last_order.total_price}.")
            else:
                print("Kode promo tidak valid atau sudah digunakan.")

        elif choice == "7":
             display_token_menu(active_user)
             
        elif choice == "8":
            print("\n=== Top-Up Game ===")
            if not active_user:
                print("Silakan pilih pengguna aktif terlebih dahulu.")
                continue
            print("Daftar Top-Up Game:")
            for idx, game in enumerate(games, start=1):
                print(f"{idx}. {game.display_game_info()}")
            try:
                game_choice = int(input("Pilih game (nomor): "))
                selected_game = games[game_choice - 1]
                quantity = input("Masukkan jumlah: ")
                create_order(selected_game, quantity)
            except (IndexError, ValueError):
                print("Pilihan game tidak valid.")

        elif choice == "9":
            print("\n=== Bayar Tagihan ===")
            if not active_user:
                print("Silakan pilih pengguna aktif terlebih dahulu.")
                continue

            print("Daftar Tagihan:")
            for idx, bill in enumerate(bills, start=1):
                print(f"{idx}. Nama: {bill.name}, Jumlah: Rp{bill.amount}, Tanggal Jatuh Tempo: {bill.due_date}")
            try:
                bill_choice = int(input("Pilih tagihan (nomor): "))
                selected_bill = bills[bill_choice - 1]

                # Membuat objek item khusus untuk tagihan
                class TagihanItem:
                    def __init__(self, name, price):
                        self.name = name
                        self.price = price

                    def display_item_info(self):
                        return f"{self.name} - Rp{self.price}"

                # Membuat objek tagihan sebagai item
                bill_item = TagihanItem(selected_bill.name, selected_bill.amount)

                # Menambahkan pembayaran tagihan ke daftar pesanan
                order_id = len(transaction_manager.orders) + 1
                transaction_manager.create_order(order_id, active_user, bill_item, 1)

                print(f"Tagihan '{selected_bill.name}' sejumlah Rp{selected_bill.amount} berhasil dibayar dan dicatat sebagai pesanan!")
            except (IndexError, ValueError):
                    print("Pilihan tagihan tidak valid.")

                    print("\n=== Bayar Tagihan ===")
                    if not active_user:
                        print("Silakan pilih pengguna aktif terlebih dahulu.")
                        continue

                    print("Daftar Tagihan:")
                    for idx, bill in enumerate(bills, start=1):
                        print(f"{idx}. Nama: {bill.name}, Jumlah: Rp{bill.amount}, Tanggal Jatuh Tempo: {bill.due_date}")
                    try:
                        bill_choice = int(input("Pilih tagihan (nomor): "))
                        selected_bill = bills[bill_choice - 1]

                        # Menambahkan pembayaran tagihan ke daftar pesanan
                        order_id = len(transaction_manager.orders) + 1
                        transaction_manager.create_order(order_id, active_user, {
                            "name": selected_bill.name,
                            "price": selected_bill.amount
                        }, 1)

                        print(f"Tagihan '{selected_bill.name}' sejumlah Rp{selected_bill.amount} berhasil dibayar dan dicatat sebagai pesanan!")
                    except (IndexError, ValueError):
                        print("Pilihan tagihan tidak valid.")


        elif choice == "10":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
