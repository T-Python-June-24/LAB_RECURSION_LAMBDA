'''vowels = "aeiouAEIOU"
def vowelsC(vol):

    count = 0
    for x in vol:
        if x in vowels:
            count += 1
    return count

vol = "I love python"
print("The number of vowels is", vowelsC(vol))'''

vowels = "aeiouAEIOU"

def vowelsC(vol):
    if not vol:
        return 0
    elif vol[0] in vowels:
        return 1+vowelsC(vol[1:])
    else:
        return vowelsC(vol[1:])

vol = "I love python"
print("The number of vowels is", vowelsC(vol))