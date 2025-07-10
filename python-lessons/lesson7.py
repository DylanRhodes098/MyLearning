word = "banana"

letter_counts = {}

for letter in word:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

print(letter_counts)


