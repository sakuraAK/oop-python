class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"Temperature cannot be lower than -273.15 celcius")

        self.__celsius = value


    @property 
    def fahrenheit(self):
        return self.__celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        tmp_value_celsius =  (value - 32)*5/9
        self.celsius = tmp_value_celsius



t = Temperature(10)


t.fahrenheit = -460


print(t.celsius)

