import os

userFolder = input("Your Folder: ")

file_extensions = {}
total = 0

for roots, dirs, files in os.walk(userFolder):
    for file in files:
        total += 1

        # Split filename and extension
        name, ext = os.path.splitext(file)

        # Update count for this extension
        file_extensions[ext] = file_extensions.get(ext, 0) + 1

print(f"Found {total} files.\n")

print("Extensions found:")
for ext, count in file_extensions.items():
    print(f"{ext}: {count}")
