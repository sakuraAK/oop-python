class Example:
    def __new__(cls):
        print("Constructor (__new__) is running")
        return super().__new__(cls)

    def __init__(self):
        print("Initializer (__init__) is running")

obj = Example()