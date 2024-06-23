vowels = "aeiouAEIOU"
def vowelsC(vol):

    count = 0
    for x in vol:
        if x in vowels:
            count += 1
    return count

vol = "I love python"
print("The number of vowels is", vowelsC(vol))
