str = "I love python"
vowels = ['a', 'e', 'i', 'o', 'u']

vowelsFound = filter(lambda char: char.lower() in vowels, str)
vowelsList = list(vowelsFound)
print(len(vowelsList))

