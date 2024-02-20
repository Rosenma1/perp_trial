# determing the function of finding a prime number 

def prime_finder(number):
    is_prime = True
    for num in range(2, number):
      if number % num == 0:
         is_prime = False 
         break
    if is_prime:
       print('This a prime number')
    else:
       print('This is not a prime number')

number = int(input('enter a number: ')) 
prime_finder(number)

