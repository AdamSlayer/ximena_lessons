class Computer():
    def __init__(self, computer, ram, storage):
            self.computer = computer
            self.ram = ram
            self.storage = storage

class Mobile(Computer):
    def __init__(self, computer, ram, storage, model):
        super().__init__(computer, ram, storage)
        self.model = model

apple = Mobile('Apple', 4, 128, 'Iphone X')

print("The mobile is: ", apple.computer)
print("The ram is: ", apple.ram)
print("The storage is: ", apple.storage)
print("The model is: ", apple.model)