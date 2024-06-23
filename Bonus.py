
def fizzBuzz_forloop(number:int):
    for i in range(1,number+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")    
        else:
            print(i) 

def fizzBuzz_whileloop(number:int): 
    i:int=1
    while i!=101:
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")    
        else:
            print(i) 
        i=i+1    
print("fizzBuzz using for loop")
fizzBuzz_forloop(100)

print("------------------------------------------------")

print("fizzBuzz using while loop")
fizzBuzz_whileloop(100)
