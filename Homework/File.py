file = open("file.txt", "r")
text = file.read()
print(text)

text = "Hello world"
file2 = open("file2.txt", "w")

file2.write(text)
file2.close()
file.close()
