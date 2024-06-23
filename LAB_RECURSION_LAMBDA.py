def vowels(phrase:str) -> int:
    if len(phrase) == 0:
        return 0
    elif phrase[0].lower() in "aeiou":
        return 1 + vowels(phrase[1:])
    else:
        return 0 + vowels(phrase[1:])
text:str = "I love python"
print(vowels(text))

numbers:list = [40, 35, 10, 15, 20]
squared_numbers:list = list(map(lambda number: number ** 2, numbers))
print(squared_numbers)
