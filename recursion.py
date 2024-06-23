#part 1
def count_vowels(phrase):
    vowels = "aeiou"
    
    # Base case
    if not phrase:
        return 0
    
    first_char = phrase[0].lower()
    if first_char in vowels:
        return 1 + count_vowels(phrase[1:])
    else:
        return 0 + count_vowels(phrase[1:])


phrase = "I love python"
print(count_vowels(phrase))  


# Part 2
numbers = [40, 35, 10, 15, 20]

squared_numbers = list(map(lambda x: x * x, numbers))

print(squared_numbers)
