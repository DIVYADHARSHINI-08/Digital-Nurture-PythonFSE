from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")


device = MultiFunctionPrinter()

device.print_document()
device.scan_document()