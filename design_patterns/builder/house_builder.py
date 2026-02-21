from abc import ABC, abstractmethod
from house import BuilderHouse

class HouseBuilderInterface(ABC):

    def __init__(self):
        self.new_house()
    
    def get_house(self) -> BuilderHouse:
        return self._house

    def new_house(self):
        self._house = BuilderHouse()

    @abstractmethod
    def prep_foundation(self):
        pass

    @abstractmethod
    def construct_walls(self):
        pass

    @abstractmethod
    def install_windows(self):
        pass

    @abstractmethod
    def put_roof(self):
        pass

    @abstractmethod
    def build_basement(self):
        pass

    @abstractmethod
    def do_interior(self):
        pass

    @abstractmethod
    def add_garage(self):
        pass
    

class StandardHouseBuilder(HouseBuilderInterface):
    def prep_foundation(self):
        self.get_house().foundation = "Reinforced concrete"

    def construct_walls(self):
        self.get_house().walls = "Red bricks"

    def install_windows(self):
        self.get_house().windows = "White vinyl double"

    def put_roof(self):
        self.get_house().roof = "Shingles"


    def build_basement(self):
        self.get_house().basement = "Finished"

    def do_interior(self):
        self.get_house().interior = "Farmhouse"

    def add_garage(self):
        pass
    
class StandardHouseWithGarageBuilder(StandardHouseBuilder):
    def add_garage(self):
        self.get_house().garage = "2 cars"
        

class IglooBuilder(HouseBuilderInterface):
    def prep_foundation(self):
        self.get_house().foundation = "Ice"

    def construct_walls(self):
        self.get_house().walls = "Ice blocks"

    def install_windows(self):
        self.get_house().windows = "None"

    def put_roof(self):
        self.get_house().roof = "Dome shape"

    def build_basement(self):
        self.get_house().basement = "None"

    def do_interior(self):
        self.get_house().interior = "Cold"

    def add_garage(self):
        self.get_house().garage = "None"