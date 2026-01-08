months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#1. Lambda function calculating kinetic energy KE=(m*v**2)/2
kinetic_energy = lambda m,v: (m*v**2)/2
print("Kinetic Energy: ", kinetic_energy(12,2),"J")

#2. Lambda function calculating mass energy E=m*c**2
mass_energy = lambda m,c=299792458: m*c**2
print("Mass Energy: ", mass_energy(0.000002),"J")

#3. Lambda function calculating gravitational force F=G*m1*m2/r**2
gravitational_force = lambda m1, m2=5.972, r=6371000: 6.67408 * 10 ** -11 * m1 * m2 / r ** 2
print("My gravitational force", gravitational_force(82,62,2),"N")

#4.Lambda function creating abbreviation for each month from a list
abv_months = list(map(lambda month: month[:3].upper(), months))

print(abv_months)
print(type(abv_months))
print(type(mass_energy))