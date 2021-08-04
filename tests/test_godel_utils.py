from src.godel_utils import (
	sequence_to_godel_number,
	godel_number_to_sequence,
	encode_pair,
	decode_pair,
)

from .test_utils.test_utils import gen


def test_sequence_to_godel_number():
	"""Test converting sequence to Gödel number"""
	assert sequence_to_godel_number(gen()) == 1
	assert sequence_to_godel_number(gen(1)) == 2
	assert sequence_to_godel_number(gen(0, 1)) == 3
	assert sequence_to_godel_number(gen(1, 2, 3)) == 2250


def test_godel_number_to_sequence():
	"""Test converting godel number to sequence"""
	assert godel_number_to_sequence(1) == ()
	assert godel_number_to_sequence(2) == (1,)
	assert godel_number_to_sequence(3) == (0, 1)
	assert godel_number_to_sequence(2250) == (1, 2, 3)


def test_encode_pair():
	"""Test encoding a pair"""
	assert encode_pair(0, 0) == 0
	assert encode_pair(1, 0) == 1
	assert encode_pair(0, 1) == 2
	assert encode_pair(4, 6) == 207


def test_decode_pair():
	"""Test decoding a pair"""
	assert decode_pair(0) == (0, 0)
	assert decode_pair(1) == (1, 0)
	assert decode_pair(2) == (0, 1)
	assert decode_pair(207) == (4, 6)
