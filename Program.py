# def vowelsCounter(word:str) -> str:
    
#     if not word:
#         return 0
#     if word[0].lower() in "aeiou":
#         return 1  + vowelsCounter(word[1:])
#     else:
#         return  vowelsCounter(word[1:])

# print(vowelsCounter("I love python"))


listOfNumber:int = [40,35, 10, 15, 20]

multiplyedList:int = list(map(lambda x: x * x, listOfNumber))

print(multiplyedList)