with open ("example.text", "w") as file:
    file.write("Hello, this is a test file \n It has multiple lines.")

with open ("example.text", "r") as file:
    print(file.read())

with open ("example.text", "w") as file:
    file.write("This file has been overwitten")
