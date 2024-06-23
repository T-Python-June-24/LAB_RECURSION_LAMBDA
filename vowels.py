str = "I love python"
vowels = ['a', 'e', 'i', 'o', 'u']

vowelsFound = filter(lambda char: char.lower() in vowels, str)
vowelsList = list(vowelsFound)
print(len(vowelsList))





numbers = [40,35, 10, 15, 20]
def multply(num):
    return num * num
numbersMultiplication = map(multply,numbers)
print(list(numbersMultiplication))