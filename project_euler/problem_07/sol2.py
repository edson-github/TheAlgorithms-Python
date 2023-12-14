# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the Nth prime number?
def isprime(number):
	return all(number%i != 0 for i in range(2, int(number**0.5)+1))
n = int(input('Enter The N\'th Prime Number You Want To Get: ')) # Ask For The N'th Prime Number Wanted
primes = []
num = 2
while len(primes) < n:
	if isprime(num):
		primes.append(num)
	num += 1
print(primes[-1])
