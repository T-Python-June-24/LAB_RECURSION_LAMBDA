
#LAB (1)
str = "I love python"
vowels = ['a', 'e', 'i', 'o', 'u']

vowelsFound = filter(lambda char: char.lower() in vowels, str)
vowelsList = list(vowelsFound)
print(len(vowelsList))




#LAB (2)
numbers = [40,35, 10, 15, 20]

numbersMultiplication = map(lambda num: num **2 ,numbers)
print(list(numbersMultiplication))

