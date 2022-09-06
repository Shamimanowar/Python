from abc import ABC, abstractmethod


class Vehicle(ABC):
    
    def __init__(self, name=None, manufacturer=None, color=None):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        
    @abstractmethod
    def get_properties(self):
        return list(zip([self.name, self.manufacturer, self.color], ["name", "manufacturer", "color"]))


class Car(Vehicle):
    
    def __init__(self, name, manufacturer, color, wheel):
        super().__init__(name, manufacturer, color)
        self.wheel = wheel
    
    def get_properties(self):
        return list(zip([self.name, self.manufacturer, self.color, self.wheel], ["name", "manufacturer", "color", "wheel"]))
    
    def drive(self, driver_name):
        print("Hello {0}!, Welcome here to drive the {1}".format(driver_name, self.name))
        
        
if __name__ == "__main__":
    car = Car("shamimCar", "Shamim Anowar", "red", 8)
    print(car.get_properties())
    car.drive("SA")
    # vehicle = Vehicle()
    