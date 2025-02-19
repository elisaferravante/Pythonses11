print(type(6/2))

print(type(5 and 7.2))
print(type(5 or 6))
type(print(2*2))
print(type("".find))
print(type("123".upper()))

print([] or "" or 0/10 or 7/2 or 9)
print(9 and 10 and 7/2 and ""and 11/2)

a=2
b=3
c="abc"
print(a,b,c)


name = input("enter your name: ")
print(f"hello, {name}!")

number1 = int(input("give me one number"))
number2 = int(input("give me another number"))
print("sum:",number1 + number2)
print("difference:", number1 - number2)
print("product:", number1 * number2)
print("quotient:", number1 / number2)

#functions - show prime numbers from list
def is_prime(num):
    """Function to check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_numbers(numbers):
    """Function to return prime numbers from a list."""
    primes = [num for num in numbers if is_prime(num)]
    return primes

# Example usage
numbers = [10, 15, 17, 19, 21, 23, 29, 30, 31]
print(f"Original list: {numbers}")
print(f"Prime numbers: {get_prime_numbers(numbers)}")



#find 3 letter words starting with b inside file
def find_words(filename): #defining our function
    """
    prints 3 letter words starting with b from a file
    :param filename: the name of file
    :return: none(nothing)
    """
    with open(filename) as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) == 3 and word[0] in "bB":
                    print(word)

find_words("input.txt")

