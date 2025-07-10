import os

userFile = "/Users/dylanrhodes/Documents/all-coding/coding-bootcamp/MyLearning"
os.chdir(userFile)
listofFile = os.listdir(userFile)
for items in listofFile:
    if os.path.isdir(items):
        print("isfolder", items)
    else:
        print("isfile", items)

total = 0
for roots, dir, files in os.walk(userFile):
    total += len(files)

print(total)
