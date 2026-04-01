# demonstrating file handling operations in python 

# 1. open a file in write mode and write data
file = open("demo_file.txt", "w")
file.write("Hello! This is the first line in the file.\n")
file.write("Python file handling demonstration.\n")
file.close()  # properly closing the file 

print("Data written successfully.\n")

# 2. open the file in read mode and read contents 
file = open("demo_file.txt", "r")
print("Reading file contents:")
content = file.read()
print(content)
file.close()

# 3. open the file in append mode and add more content 
file = open("demo_file.txt", "a")
file.write("This line is added using append mode.\n")
file.write("File handling in Python is easy!\n")
file.close()

print("Data appended successfully.\n")

# 4. read the file again to see updated content
file = open("demo_file.txt", "r")
print("Reading updated file contents:")
content = file.read()
print(content)
file.close()