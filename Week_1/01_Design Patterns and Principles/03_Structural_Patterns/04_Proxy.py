class RealServer:
    def request(self):
        print("Accessing Server")


class Proxy:
    def __init__(self):
        self.server = RealServer()

    def request(self):
        print("Checking Access...")
        self.server.request()


proxy = Proxy()
proxy.request()