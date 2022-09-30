def prime_factors(num):
	"""
	prime(num) returns the prime factors of num.

	>>> prime_factors(12)
	[2, 2, 3]
	"""
	factors = []

	if num < 2:
		return None

	while num % 2 == 0:
		factors.append(2)
		num = num/2

	for i in range(3, int(num)+1, 2):
		while num % i == 0:
			factors.append(i)
			num = num/i

	return factors


def prime_factors_class(n):
	"""
	>>> prime_factors_class(8)
	2
	2
	2

	>>> prime_factors_class(11)
	11
	"""
	while n > 1:
		s = smallest_prime_factor(n)
		n = n // s
		print(s)

def smallest_prime_factor(n):
	k = 2
	while k <= n:
		if n % k == 0:
			return k 
		k+=1
		