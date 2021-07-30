from typing import List, Tuple

from primes import prime_generator


def godel_number_to_sequence(godel_number: int) -> List[int]:
	"""calculate the sequence numbers given the godel number"""
	code = []
	for prime in prime_generator():
		if godel_number <= 1:
			break
		instruction = 0
		while godel_number % prime == 0:
			instruction += 1
			godel_number = godel_number / prime
		code.append(instruction)
	return code


def encode_pair(x: int, y: int) -> int:
	"""encode a pair of numbers"""
	return 2 ** x * (2 * y + 1) - 1


def decode_pair(z: int) -> Tuple[int, int]:
	"""Return left and right given a pair encoding"""
	x, y = 0, z
	# divide y by 2 until it is even
	while y % 2 != 0:
		x += 1
		y = y // 2
	# x is the power of 2
	# y is half of the remaining even number
	return x, y // 2
