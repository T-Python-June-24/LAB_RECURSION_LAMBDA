def fizzbuzz(number_of_iterations):
    for num in range(1, number_of_iterations+1):
        print('Fizz'*(num%3==0) + 'Buzz'*(num%5==0) or num)

try:
    fizzbuzz(15)
except Exception as e:
    print(e)

def fizzbuzz_while(number_of_iterations):
    counter = 1
    while counter <= number_of_iterations:
        print('Fizz'*(counter%3==0) + 'Buzz'*(counter%5==0) or counter)
        counter += 1

try:
    fizzbuzz_while(15)
except Exception as e:
    print(e)
