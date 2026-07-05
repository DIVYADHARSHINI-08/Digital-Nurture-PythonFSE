class Light:
    def on(self):
        print("Light ON")


class LightOnCommand:
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


light = Light()
command = LightOnCommand(light)

command.execute()