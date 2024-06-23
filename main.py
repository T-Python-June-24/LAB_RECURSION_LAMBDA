def vowels_recursion(word):
    """
    This function counts the number of vowels in a word using recursion.
    
    It has 3 cases:
    1. If the word is empty, return 0.
    2. If the first letter is a vowel, return 1 + the number of vowels in the rest of the word,
    so if we input "I love python", the function will return 1 + the number of vowels in "love python", which is 1.
    
    3. If the first letter is not a vowel, return the number of vowels in the rest of the word.
    so if we input "I love python", the function will return the number of vowels in "love python", which is 0.

    and so on till the last index
    
    Args:
        word (str): The word to count the number of vowels in.

    Returns:
        int: The number of vowels in the word.
    """
    vowels_letters = 'aeiouAEIOU'
    first_letter = word[0]
    rest_of_the_word = word[1:]
    if word == "":
        return 0
    elif first_letter not in vowels_letters:
        return vowels_recursion(rest_of_the_word)
    else: # the 1 here is for counting the first letter whether it's a vowel or not
        return 1 + vowels_recursion(rest_of_the_word)
    
try:  
    print(vowels_recursion("I love python"))
except Exception as e:
    print(e)


nums = [40,35, 10, 15, 20]
num_square = list(map(lambda x: x**2, nums))

try:
    print(f"num_square: {num_square}, nums: {nums}")
except Exception as e:
    print(e)