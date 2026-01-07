my_friends = ['Alice', 'Bob', 'Charlie']
your_friends = ['John', 'Doe', 'Kevin']

print(my_friends+your_friends)

my_friends += your_friends

people = list(my_friends)
my_friends[4] = 'Jane'
print(my_friends)
print(people)