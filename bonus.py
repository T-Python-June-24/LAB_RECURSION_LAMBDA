number_divisible_by_3 = lambda num: num % 3 == 0
number_divisible_by_5 = lambda num: num % 5 == 0

def FizzBuzz_for(number_of_iterations):
    
    for number in range(1, number_of_iterations+1):
        if number_divisible_by_3(number) and number_divisible_by_5(number):
            print("FizzBuzz")
        elif number_divisible_by_3(number):
            print("Fizz")
        elif number_divisible_by_5(number):
            print("Buzz")
        else:
            print(number)

try:
    FizzBuzz_for(15)
except Exception as e:
    print(e)
 
# fizzbuzz solution using recursion
def FizzBuzz_while(number_of_iterations):
    counter = 1
    while counter <= number_of_iterations:
        if number_divisible_by_3(counter) and number_divisible_by_5(counter):
            print("FizzBuzz")
        elif number_divisible_by_3(counter):
            print("Fizz")
        elif number_divisible_by_5(counter):
            print("Buzz")
        else:
            print(counter)
        counter += 1
           
        
    
try:
    FizzBuzz_while(15)
except Exception as e:
    print(e)    