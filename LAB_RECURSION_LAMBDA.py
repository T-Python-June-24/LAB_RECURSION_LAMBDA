def countVowels(word: str, count=0) -> int:
    vowels = ('a', 'e', 'i', 'o', 'u')
    word = word.lower()
    
    if not word:
        return count
    
    if word[0] in vowels:
        count += 1
    
    return countVowels(word[1:], count)

print(countVowels("I love python"))

# problem 2
randomNumbers:list=[40,35, 10, 15, 20]
result=map(lambda x:x*x,randomNumbers)
print(list(result))

