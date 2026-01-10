class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print("meooooowwwww")

class Leopard(Cat):
    def vocalize(self):
        print("whrghhhh")

class Cheetah(Cat):
    def vocalize(self):
        print("eeeeeeeeee")

tommy = Cat(5,17,16)
tommy.vocalize()

leo = Leopard(90,30,27)
leo.vocalize()

cheetah = Cheetah(300,90,27)
cheetah.vocalize()

print(leo.__dict__)