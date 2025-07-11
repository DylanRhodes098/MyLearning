word = input ("add word: ")
wordLower = word.lower()
vowels = ["a", "e", "i", "o", "u"]

count = 0
for letters in wordLower:
    if letters in vowels:
        count += 1

print(f"{wordLower} has {count} vowels")