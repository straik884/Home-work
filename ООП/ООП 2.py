class Transport:
    name = 'Mzda'
    max_speed = 210
    mileage = 200

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacite=50):
        return f'Вместимость одного автобуса {self.name} {capacite} пасажиров'



Autobus = Transport('Renault Logan', 180, 12)


print(Autobus.seating_capacity())