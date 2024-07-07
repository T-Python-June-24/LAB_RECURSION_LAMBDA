
#LAB (1)
word = "I love python"
vowels = ['a', 'e', 'i', 'o', 'u']

def vowelsIn(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word == '':
        return ''
    elif word[0].lower() in vowels and word != '':
        return word[0] + vowelsIn(word[1:])
    else:
        return vowelsIn(word[1:])
    
total_vowels = len(vowelsIn(word))           
print(f"The total vowels in ({word}) is {total_vowels} vowels.")


# Another way:

# vowelsFound = filter(lambda char: char.lower() in vowels, str)
# vowelsList = list(vowelsFound)
# print(len(vowelsList))



#LAB (2)
numbers = [40,35, 10, 15, 20]

numbersMultiplication = map(lambda num: num **2 ,numbers)
print(list(numbersMultiplication))

