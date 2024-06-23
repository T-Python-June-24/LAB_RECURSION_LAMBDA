# Q1
def vowels (x):
 vowel = {'a', 'e', 'i', 'o', 'u'}

 if not x:
      return 0
 first_char = x[0].lower()
 count = 1 if first_char in vowel else 0
 return count + vowels(x[1:])
phrase = "I love python"
print(vowels(phrase)) 



print(" -"*15)


#Q2
numbers = [40,35, 10, 15, 20]

new_list = map( lambda num: num * num , numbers)

print(list(new_list))
