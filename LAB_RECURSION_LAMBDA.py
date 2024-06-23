# Q1

def count_vowels(inputStr):
    """
    Recursively counts the number of vowels in a given string.
    
    Args:
        inputStr (str): The string to count the vowels in.
        
    Returns:
        int: The number of vowels in the input string.
    """
    vowels = ("a","e","i","o","u")

    if not inputStr:
        return 0

    firstChar = inputStr[0].lower()

    if firstChar in vowels:

        return 1 + count_vowels(inputStr[1:])
    else:

        return count_vowels(inputStr[1:])

phrase = "I love python"
try:

    num_vowels = count_vowels(phrase)
    print(f"\033[2J\033[32mThe solution of Q1 : count of vowels in '{phrase}' = {num_vowels} \n ")  

except Exception as e:
    print(f"\033[31mError: {e}")

# Q2

numbers = [40,35, 10, 15, 20]
try:
    multipliedByItself = list(map(lambda x: x*x, numbers))
    print(f"\033[32mThe solution of Q2 : {numbers} * {numbers} = {multipliedByItself} \n") 
    
except Exception as e:
    print(f"\033[31mError: {e}\n")

