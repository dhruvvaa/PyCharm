person = "Jeff"
petName = "Rex"
petType = "Dog"

print(person, 'has a', petType, 'and his name is ', petName)
print(f"{person} has a {petType} and his name is {petName}")

m = '{} has a {}and his name is {}.'
print(m.format(person, petType, petName))
print('%s has a %s and his name is %s.'%(person, petType, petName))