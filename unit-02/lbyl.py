import os

filename = "data.txt"

if os.path.exists(filename):
    file = open(filename, "r")
    print(file.read())
    file.close()
else:
    print(f"The file '{filename}' does not exist.")
