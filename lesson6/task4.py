
class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
    
    def car_name(self):
        print(self.name)
    
    def go(self):
        print('going')
        
    def stop(self):
        print('stoped')
        
    def turn(self, direction):
        print(f'turning {direction}')
        
        
class TownCar(Car):
    def __init__(self, *args):
        self.overspeed = 60
        super().__init__(*args)
        
    def show_speed(self):
        print(f'Current speed: {self.speed}')
        if self.speed > self.overspeed:
            print(f'Speeding by {self.speed-self.overspeed}')
        
        
class SportCar(Car):
    def show_speed(self):
        print(f'Current speed: {self.speed}')
        
        
class WorkCar(Car):
    def __init__(self, *args):
        self.overspeed = 40
        super().__init__(*args)
        
    def show_speed(self):
        print(f'Current speed: {self.speed}')
        if self.speed > self.overspeed:
            print(f'Speeding by {self.speed-self.overspeed}')
        
        
class PoliceCar(Car):
    def show_speed(self):
        print(f'Current speed: {self.speed}')
        
        

tc = TownCar('TownCar', 'black', 70, False)
sc = SportCar('SportCar', 'black', 70, False)
wc = WorkCar('WorkCar', 'black', 70, False)
pc = PoliceCar('PoliceCar', 'black', 70, True)

for i in [tc, sc, wc, pc]:
    i.car_name()
    i.show_speed()
    i.go()
    i.stop()
    i.turn('left')
    i.turn('right')
    print(i.is_police)
    print()
