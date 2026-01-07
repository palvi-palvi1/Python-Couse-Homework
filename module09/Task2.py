class Elevator:
    def __init__(self, bottom_floor , top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"elevator is now at  floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"elevator is now at  floor {self.current_floor}")

    def go_to_floor(self, target_floor):
            if target_floor > self.top_floor:
                print(f"floor {target_floor} is out of range")

            while self.current_floor < target_floor:
               self.floor_up()
            while self.current_floor > target_floor:
                self.floor_down()




class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators= []

        for i in range(number_of_elevators):
         self.number_of_elevators.append(Elevator(bottom_floor, top_floor))
    def run_elevator(self, elevator_number, destination_floor):
        self.number_of_elevators[elevator_number - 1].go_to_floor(destination_floor)




new_building = Building(1,7,2)

print("moving elevator 1 to  floor 4")
new_building.run_elevator(1, 4)

print("moving  elevator 2 to floor 3")
new_building.run_elevator(2, 3)

