# The prime 41, can be written as the sum of six consecutive primes:
# This is the longest sum of consecutive primes that adds to a prime
# below one-hundred.
#     41 = 2 + 3 + 5 + 7 + 11 + 13
# The longest sum of consecutive primes below one-thousand that adds
# to a prime, contains 21 terms, and is equal to 953
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

# =======================================================================
# =======================================================================

# This program generates a list of prime numbers up to a given limit.
# It uses the Sieve of Eratosthenes algorithm to efficiently find primes.
# The program first initializes a list of integers from 0 to the limit,
# with 0 and 1 marked as not prime. It then iterates through the list,
# marking all multiples of each prime number as not prime. The remaining
# numbers are prime and are added to a separate list. The program prints
# the length of the list of primes and the largest prime number found.

# RU: Эта программа генерирует список простых чисел до заданного предела.
# Она использует алгоритм решета Эратосфена для эффективного поиска простых чисел.
# Программа сначала инициализирует список целых чисел от 0 до предела,
# с 0 и 1 помеченных как не простые. Затем она перебирает список,
# помечая все кратные каждого простого числа как не простые. Оставшиеся
# числа являются простыми и добавляются в отдельный список. Программа печатает
# длину списка простых чисел и наибольшее найденное простое число.

# =======================================================================
# =======================================================================

# Set the limit for finding primes
limit = 1000000


# Set the limit for finding primes
limit = 1000000

# Create a list of integers up to the limit, with 0 and 1 marked as not prime
is_prime = [True] * limit

# Create an empty list to store prime numbers
prime_numbers = []

# Mark 0 and 1 as not prime
is_prime[0] = is_prime[1] = False

# Iterate through the list of integers
for number in range(2, limit):
    # If the current number is prime
    if is_prime[number]:
        # Add it to the list of primes
        prime_numbers.append(number)
        # Mark all multiples of the current prime as not prime
        for multiple in range(number * number, limit, number):
            is_prime[multiple] = False

# Print "done" to indicate the program has finished
print("done")

# Print the number of primes found
print(len(prime_numbers))

# Print the largest prime found
print(prime_numbers[-1])

# Print 100 primes
print(prime_numbers[0:100])

# Set max_sum to 0 and max_consecutive_primes to -1
max_sum = 0
max_consecutive_primes = -1

# Iterate through the list of prime numbers
for i in range(0, len(prime_numbers)):
    # Set current_sum to 0
    current_sum = 0
    # Iterate through the remaining prime numbers
    for j in range(i, len(prime_numbers)):
        # Add the current prime number to the sum
        current_sum += prime_numbers[j]
        # If the sum is greater than the limit, break out of the loop
        if current_sum > limit:
            break

        # If the sum is greater than the current max_sum
        # and the number of consecutive primes is greater
        # than the current max_consecutive_primes, update
        # the max_sum and max_consecutive_primes
        if current_sum > max_sum and j - i > max_consecutive_primes:
            max_consecutive_primes = j - i
            max_sum = current_sum

print("max_sum: ", max_sum)
print("максимум последовательность простых: ", max_consecutive_primes)
