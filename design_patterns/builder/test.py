from house import House
from engineer import Engineer
from house_builder import StandardHouseBuilder, StandardHouseWithGarageBuilder, IglooBuilder

def build_house():
    house = House(roof="Shingles",
                  walls="Red bricks",
                  windows="White vinyl double",
                  interior="Farmhouse",
                  basement="Finished",
                  foundation="Reinforced concrete")
    house.display()
    
    house_with_garage =  House(roof="Shingles",
                  walls="Red bricks",
                  windows="White vinyl double",
                  interior="Farmhouse",
                  basement="Finished",
                  foundation="Reinforced concrete",
                  garage="2 cars")
    house_with_garage.display()
    

def build_house_with_builder():
    engineer = Engineer(IglooBuilder())
    engineer.build()
    engineer.get_house().display()
    

build_house_with_builder()