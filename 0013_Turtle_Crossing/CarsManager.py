from Car import Car
import random

class CarsManager():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.no_cars = 10
        self.road_lines = []
        for y in range(50 - int(screen.window_height()/2), int(screen.window_height()/2) - 50 + 1, 20):
            self.road_lines.append(y)

        self.cars = []
        self.addCars()


    def addCars(self):
        self.car_positions = random.sample(self.road_lines, self.no_cars)
        x = int(self.screen.window_width()/2)

        for i in range(len(self.cars), self.no_cars):
            y = self.car_positions[i]
            self.cars.append(Car(x=x, y=y))


    def moveCars(self):
        for car in self.cars:
            car.move()


    def increaseCars(self, num=2):
        if self.no_cars + num <= len(self.road_lines):
            self.no_cars += num
        self.reset()


    def reset(self):
        self.car_positions = random.sample(self.road_lines, self.no_cars)
        x = int(self.screen.window_width()/2)

        for i in range(0, len(self.cars)):
            self.cars[i].relocate(self.car_positions[i])

        for i in range(len(self.cars), self.no_cars):
            y = self.car_positions[i]
            self.cars.append(Car(x=x, y=y))
