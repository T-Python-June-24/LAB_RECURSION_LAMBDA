# Q1
def vowels_letters(phrase):

    phrase=phrase.lower()
    if len(phrase)==0: #Base case / condition
        return 0

    vowels=["a","e","i","o","u"] 
    if phrase[0] in vowels:
        return 1 + vowels_letters(phrase[1:]) #recrsive case if the letter is vowel

    else:
        return vowels_letters(phrase[1:])#recrsive case if not



print(vowels_letters("I love python"))




#Q2
my_list=[40,35, 10, 15, 20]
multiplayedlist=map(lambda  item: item*item ,my_list)
print(list(multiplayedlist))
