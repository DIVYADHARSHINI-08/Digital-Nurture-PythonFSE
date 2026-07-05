class OldPrinter:
    def old_print(self):
        return "Printing using old printer"


class Adapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self):
        return self.old_printer.old_print()


printer = Adapter(OldPrinter())
print(printer.print())