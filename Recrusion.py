def countV(phrase):
    vowels= 'aeiouAEIOU'

    if not phrase:
        return 0
    
    return (1 if phrase[0] in vowels else 0) + countV(phrase[1:])
    

print(countV("I love python"))