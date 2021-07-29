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


def get_left_right(pair_number: int) -> Tuple[int, int]:
	"""return left and right given a pair encoding"""
	for x in range(pair_number + 1):
		for y in range(pair_number + 1):
			if encode_pair(x, y) == pair_number:
				return x, y