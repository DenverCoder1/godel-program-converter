from src.primes import prime_generator, is_prime


def test_prime_generator():
	"""Test prime generator"""
	primes = prime_generator()
	assert next(primes) == 2
	assert next(primes) == 3
	assert next(primes) == 5
	assert next(primes) == 7
	assert next(primes) == 11
	assert next(primes) == 13


def test_is_prime():
	"""Test is_prime function"""
	assert not is_prime(0)
	assert not is_prime(1)
	assert is_prime(2)
	assert is_prime(3)
	assert not is_prime(4)
	assert is_prime(5)
	assert is_prime(7)
