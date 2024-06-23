#1 Recursion exercise
phrase = str(input("please enter a string: "))
vowels = "aeiou"

def count_vowels(phrase):
	# Base case: if the string is empty, return 0
	if not phrase:
		return 0
	# Check if the first character is a vowel
	if phrase[0].lower() in vowels:
		return 1 + count_vowels(phrase[1:])
	else:
		return count_vowels(phrase[1:])


print("Number of vowels:", count_vowels(phrase))


#2 lambda exercise 
numbers = [40,35, 10, 15, 20]
     
multiplied_list = list(map( lambda num: num * num , numbers ))      
print( 'The list of each number multiplied by itself:' ,multiplied_list )  


