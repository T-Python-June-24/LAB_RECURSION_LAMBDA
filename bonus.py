# with for loop 
def FizzBuzzWithFor():
    for number in range(1,101):

        if number % 3 == 0 and number % 5 ==0 :
            print("FizzBuzz")

        elif number % 3 == 0 :
            print("Fizz")

        elif number % 5 == 0 :
            print("Buzz")
        else:
            print(number)

# with while 

def FizzBuzzWithWhile():
    number = 1 
    while  number < 101 :
        if number % 3 == 0 and number % 5 ==0 :
            print("FizzBuzz")

        elif number % 3 == 0 :
            print("Fizz")
        elif number % 5 == 0 :
            print("Buzz")
        else:
            print(number)
        number+= 1


print("\033[2J\033[32msolution of FizzBuzz with for loop :---------------------------------\n")

FizzBuzzWithFor()

print("\n\033[33m solution of FizzBuzz with while loop :------------------------------\n")

FizzBuzzWithWhile()