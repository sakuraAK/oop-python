class House:
    def __init__(self, roof, walls, foundation, basement, windows, interior, garage=None):
        self.roof = roof
        self.walls = walls
        self.foundation = foundation
        self.basement = basement
        self.windows = windows
        self.interior = interior
        self.garage = garage

    def display(self):
        print('Custom House:')
        print(f'\t{"Roof":>10}: {self.roof}')
        print(f'\t{"Walls":>10}: {self.walls}')
        print(f'\t{"Windows":>10}: {self.windows}')
        print(f'\t{"Interior":>10}: {self.interior}')
        print(f'\t{"Basement":>10}: {self.basement}')
        print(f'\t{"Foundation":>10}: {self.foundation}')
        if self.garage:
            print(f'\t{"Garage":>10}: {self.garage}')

class BuilderHouse(object):
    roof: str
    walls: str
    foundation: str
    basement: str
    windows: str
    interior: str
    garage = ""


    def display(self):
        print('Custom House:')
        print(f'\t{"Roof":>10}: {self.roof}')
        print(f'\t{"Walls":>10}: {self.walls}')
        print(f'\t{"Windows":>10}: {self.windows}')
        print(f'\t{"Interior":>10}: {self.interior}')
        print(f'\t{"Garage":>10}: {self.garage}')
        print(f'\t{"Basement":>10}: {self.basement}')
        print(f'\t{"Foundation":>10}: {self.foundation}')