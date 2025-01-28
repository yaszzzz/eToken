class TagihanPLN:
    def __init__(self, bill_id, customer_name, usage_kwh, tariff_per_kwh, due_date):
        self.bill_id = bill_id
        self.customer_name = customer_name
        self.usage_kwh = usage_kwh
        self.tariff_per_kwh = tariff_per_kwh
        self.due_date = due_date

    def calculate_bill(self):
        return self.usage_kwh * self.tariff_per_kwh

    def display_bill_info(self):
        return (
            f"ID Tagihan: {self.bill_id}, Pelanggan: {self.customer_name}, "
            f"Pemakaian: {self.usage_kwh} kWh, Tarif: {self.tariff_per_kwh}/kWh, "
            f"Jatuh Tempo: {self.due_date}, Total: {self.calculate_bill()}"
        )


class TagihanWiFi:
    def __init__(self, bill_id, provider_name, package_name, price, due_date):
        self.bill_id = bill_id
        self.provider_name = provider_name
        self.package_name = package_name
        self.price = price
        self.due_date = due_date

    def display_bill_info(self):
        return (
            f"ID Tagihan: {self.bill_id}, Provider: {self.provider_name}, "
            f"Paket: {self.package_name}, Harga: {self.price}, "
            f"Jatuh Tempo: {self.due_date}"
        )


class TagihanBPJS:
    def __init__(self, bill_id, participant_name, category, price, due_date):
        self.bill_id = bill_id
        self.participant_name = participant_name
        self.category = category
        self.price = price
        self.due_date = due_date

    def display_bill_info(self):
        return (
            f"ID Tagihan: {self.bill_id}, Peserta: {self.participant_name}, "
            f"Kategori: {self.category}, Harga: {self.price}, "
            f"Jatuh Tempo: {self.due_date}"
        )
