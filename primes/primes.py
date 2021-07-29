from typing import Generator


def prime_generator() -> Generator[int, None, None]:
	"""Generator to return prime numbers one at a time"""
	yield 2
	n = 3
	while True:
		if is_prime(n):
			yield n
		n += 2


def is_prime(n: int) -> bool:
	"""check if a number is a prime number"""
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(n ** 0.5) + 1, 2):
		if n % i == 0:
			return False
	return True
