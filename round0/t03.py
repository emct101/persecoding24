word = input()
letters = []

for char in word:
  letters.append(char)

letters.insert(-1,letters[0])
letters.insert(-1,letters[1])
letters.pop(0)
letters.pop(0)

final = ''
for letter in letters:
  final += letter

print(final)
