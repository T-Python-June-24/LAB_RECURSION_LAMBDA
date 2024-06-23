# LAB_RECURSION_LAMBDA

## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase `I love python` , it should return : `4` 


## 2) Given a list of numbers : `[40,35, 10, 15, 20]`

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Note: use `map()` with a `lambda funciton`



def vowels(phrase:str) -> int:
    # vwl = ()
    # # return phrase.count('a | e | i | o | u')
    # if phrase.lower().__contains__('aeiou') == True:
    #     vwl.append()
    #     return vwl.count()
    if not phrase:
        return 0
    elif phrase[0].lower() in 'aeiou':
        return 1 + vowels(phrase[1:])
    else:
        return vowels(phrase[1:])



#gvn_vowels = "I love python"
gvn_vowels = input("Provide a word or phrase: ")

print(f'###1\n\n\nNumber of vowels in "{gvn_vowels}" is {vowels(gvn_vowels)}')





###2

print("\n\n*****\n\n\n###2\n\n")

nums = [40, 35, 10, 15, 20]

new_list = map(lambda x: x*x , nums)

print(f'{list(new_list)}\n')