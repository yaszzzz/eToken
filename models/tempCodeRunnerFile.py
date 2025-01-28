"""
        Membuat pesanan untuk berbagai jenis item seperti voucher, token PLN, top-up game, atau pembayaran tagihan.
        
        Args:
            order_id (int): ID pesanan unik.
            user (User): Objek pengguna yang membuat pesanan.
            item (Voucher/Token/Game/Tagihan): Item yang dibeli.
            quantity (int): Jumlah item.
            promo_code (str): Kode promo yang digunakan (jika ada).
            item_type (str): Jenis item yang dibeli (voucher, token, game, atau tagihan).
        """