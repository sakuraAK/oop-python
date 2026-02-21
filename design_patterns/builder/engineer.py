from house_builder import HouseBuilderInterface
from house import BuilderHouse

class Engineer:
    def __init__(self, builder: HouseBuilderInterface):
        self._builder = builder

    def get_house(self) -> BuilderHouse:
        return self._builder.get_house()

    def build(self):
        self._builder.prep_foundation()
        self._builder.build_basement()
        self._builder.construct_walls()
        self._builder.put_roof()
        self._builder.add_garage()
        self._builder.install_windows()
        self._builder.do_interior()