try:
    house_value = 100000
    house_value[2] = 200000
    print(house_value)
    with open('input.txt','r') as myinputfile:
        print("how about here")
        for line in myinputfile:
            print(line)
except FileNotFoundError:
    print("file not found")
except NameError:
    print("NameError")
except TypeError:
    print("TypeError")
finally:
    print("I show up after every exception haha")