class Operation:
    def __init__(self):
        self.nombre1 = 5
        self.nombre2 = 12

    def addition(self):
        return self.nombre1 + self.nombre2

ops = Operation()

print(ops)
print(ops.nombre1, ops.nombre2)
print(ops.addition())