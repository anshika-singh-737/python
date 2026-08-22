import os

# Print the contents of the current directory
contents = os.listdir()

print("Contents of the directory are:\n")

for item in contents:
    print(item)