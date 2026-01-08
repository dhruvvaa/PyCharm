def fancy_name_plate(*names):
    for name in names:
        print("##################")
        print("##--------------##")
        print("##" + name.center(28,'-') + "##")
        print("##---------------##")
        print("###################")

def fancy_name_plate_defargs(name, length=26, symbol="&"):
    print(symbol * length)
    print(symbol * 2 + (length - 4) * '-' + symbol * 2)
    print(symbol * 2 + name.center(length - 4, '-') + symbol * 2)
    print(symbol * 2 + (length - 4) * '-' + symbol * 2)
    print(symbol * length)

fancy_name_plate('Dhruva','You the viewer','C3PO')
fancy_name_plate_defargs('Aditya',19,'%')
fancy_name_plate_defargs('Shalvi',12,'@')