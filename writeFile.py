text = open("blank.txt", "r+")

for i in range(0,11):
    text.write(str(i)+30*'')
    text.write("\n")

text.write("The End")
text.seek(0)
text.write("The Start")