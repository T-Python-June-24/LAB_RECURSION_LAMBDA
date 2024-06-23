'''

## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase `I love python` , it should return : `4` 


'''


def vowels(pharse):
    
    pharse=pharse.lower()#vowels no matter if it is lowercase or uppercase 
    if len(pharse) == 0:
        return 0
    
    if pharse[0] in "aeiou":
        return 1 + vowels(pharse[1:])
    else:
         return vowels(pharse[1:])
   
print(vowels("I love Python"))  
     
       
     
'''
## 2) Given a list of numbers : `[40,35, 10, 15, 20]`
#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Note: use `map()` with a `lambda funciton`  
'''


numbers = [40, 35, 10, 15, 20]
squared_numbers = list(map(lambda x: x*x, numbers))
print(squared_numbers)
