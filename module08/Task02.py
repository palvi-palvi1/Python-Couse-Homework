class Car:
    def __init__(self , maximum_speed):
        self.maximum_speed = maximum_speed
        self.current_speed = 0
    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

car = Car(150)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f"crrent speed: {car.current_speed}")
car.accelerate(-200)
print(f"final speed: {car.current_speed}")
