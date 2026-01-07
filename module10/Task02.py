class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

        self.current_speed = 0
        self.distance_traveled = 0

    def drive(self, hours):
        distance_covered = self.current_speed * hours
        self.distance_traveled += distance_covered

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

    def print_information(self):
        print(f"Registration: {self.registration_number}, Max Speed: {self.maximum_speed} km/h, Battery: {self.battery_capacity} kWh")


class GasolineCar (Car):
    def __init__(self, registration_number, maximum_speed, tank_capacity):
        super().__init__(registration_number, maximum_speed)
        self.tank_capacity = tank_capacity

    def print_information(self):
        print(f"Registration: {self.registration_number}, Max Speed: {self.maximum_speed} km/h, Tank: {self.tank_capacity} l")
electric_car = ElectricCar("ABC-123","165", "52.5")

gasoline_car = GasolineCar("ACD-123", "165", "32.3")
electric_car.print_information()
gasoline_car.print_information()



