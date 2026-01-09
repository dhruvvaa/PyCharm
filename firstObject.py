#create a car class
class Car():
    pass

#create car objects
honda = Car()
mazda = Car()

#add attributes to the car object
honda.mode1 = 'CRV'
honda.weight = 1200

#print attributes in 2 different ways
print("Honda mode 1:",honda.mode1)
print("Honda weight:",honda.weight)
print(honda.__dict__)
print(mazda.__dict__)