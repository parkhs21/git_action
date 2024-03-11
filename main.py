import os

print()
print(os.getcwd())
print(file_list := os.listdir())

for file in file_list:
    if file.endswith(".py"):
        print()
        print(open(file).read())