from typing import Generator, Tuple

from src.primes import prime_generator


def sequence_to_godel_number(sequence: Generator[int, None, None]) -> int:
	"""
	Converts a sequence of numbers into a Gödel number

	Gödel(a_1, ..., a_n) = p_1 ^ a_1 * ... * p_n ^ a_n

	where p_i is the ith prime number and a_i is the ith element in the sequence
	"""
	product = 1
	for prime in prime_generator():
		try:
			product *= prime ** next(sequence)
		except StopIteration:
			break
	return product


def godel_number_to_sequence(godel_number: int) -> Tuple[int]:
	"""Calculate the sequence numbers given the Gödel number"""
	code = []
	for prime in prime_generator():
		# if remaining number is 1, all remaining powers are 0
		if godel_number <= 1:
			break
		# count number of times the prime divides the number
		instruction = 0
		while godel_number % prime == 0:
			instruction += 1
			godel_number = godel_number // prime
		code.append(instruction)
	return tuple(code)


def encode_pair(x: int, y: int) -> int:
	"""Encode a pair of numbers"""
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
