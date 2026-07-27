class Invoice:
    def __init__(self, amount):
        self.amount = amount

    def calculate_total(self):
        return self.amount


class InvoicePrinter:
    def print_invoice(self, invoice):
        print(f"Invoice Amount: ₹{invoice.calculate_total()}")


invoice = Invoice(2500)
printer = InvoicePrinter()
printer.print_invoice(invoice)