class Computer:

    def __init__(self):
        self.cpu = ""
        self.ram = ""

    def show(self):
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram}")


class ComputerBuilder:

    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def build(self):
        return self.computer


computer = (
    ComputerBuilder()
    .set_cpu("Intel i7")
    .set_ram("16 GB")
    .build()
)

computer.show()