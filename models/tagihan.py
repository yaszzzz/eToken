class Tagihan:
    def __init__(self, bill_id, name, amount, due_date):
        self.bill_id = bill_id
        self.name = name
        self.amount = amount
        self.due_date = due_date

    def display_bill_info(self):
        return (
            f"ID Tagihan: {self.bill_id}\n"
            f"Nama: {self.name}\n"
            f"Jumlah: Rp{self.amount:,}\n"
            f"Tanggal Jatuh Tempo: {self.due_date}\n"
        )
