def vowelsCounter(word:str) -> str:
    #base case
    if not word:
        return 0
    if word[0].lower() in "aeiou":
        #if it's vowels, add 1 and recurse on the rest of the string
        return 1  + vowelsCounter(word[1:])
    else:
        return  vowelsCounter(word[1:])

print(vowelsCounter("I love python"))



#-------------------------------------------

listOfNumber:int = [40,35, 10, 15, 20]
# use map for iterate through a list without using an explicit loop than convert it to list
multiplyedList:int = list(map(lambda x: x * x, listOfNumber))

print(multiplyedList)