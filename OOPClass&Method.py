class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        print(f"{self.brand} is running at {self.speed} km/h")

car1 = Car("Tesla", 120)
car1.accelerate()
