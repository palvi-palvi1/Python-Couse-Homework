class Car:
    def __init__(self, travelled_distance, current_speed):
        self.travelled_distance = travelled_distance
        self.current_speed = current_speed

    def drive(self, hours):
        distance_covered = self.current_speed * hours
        self.travelled_distance += distance_covered
car = Car(200, 60)
car.drive(1.5)

print(f"total distance: {car.travelled_distance} km")


        
