#create dictionary in two different ways
scores = dict(
    Bob = 20,
    Alice = 25
)

nicknames = {'Bob': 'Bobby', 'Alice': 'Ally'}

#print dictionary
print(scores)
print(nicknames)

#read a specific value from a dictionary
print(scores['Alice'])
scores['Cam'] = 22
scores['Cam'] += 1
print(scores)