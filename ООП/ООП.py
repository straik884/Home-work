class Transport:
    name = 'Mzda'
    max_speed = 210
    mileage = 200

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def inf_car(self):
        print(f'Название автомобиля: {self.name}. Cкорость: {self.max_speed}. Пробег: {self.mileage}')


Autobus = Transport('Renault Logan', 180, 12)

Autobus.inf_car()