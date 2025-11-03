import os

folder_path = "."  # current directory
files = os.listdir(folder_path)

print("Files in this folder:")
for file in files:
    print(file)
