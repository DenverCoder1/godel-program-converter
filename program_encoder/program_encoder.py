from typing import Generator, Tuple

from godel_utils import encode_pair
from primes import prime_generator

from .constants import ADD_REGEX, GOTO_REGEX, MINUS_REGEX, NOOP_REGEX


def encode_label(label: str) -> int:
	"""Encodes a label into a number"""
	if not label:
		return 0
	index = int(label[1:]) if len(label) > 1 else 1
	offset = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}[label[0]]
	return (index - 1) * 5 + offset


def encode_var(variable: str) -> int:
	"""Encodes a label into a number"""
	if variable == "Y":
		return 1
	index = int(variable[1:]) if len(variable) > 1 else 1
	offset = {"X": 0, "Z": 1}[variable[0]]
	return index * 2 + offset


def convert_instruction(instruction: str) -> Tuple[int, int, int]:
	"""Determine the a, b, and c values for a given instruction as a string"""
	# NOOP
	if match := NOOP_REGEX.match(instruction):
		instruction_type = 0
	# ADD
	elif match := ADD_REGEX.match(instruction):
		instruction_type = 1
	# MINUS
	elif match := MINUS_REGEX.match(instruction):
		instruction_type = 2
	# GOTO
	elif match := GOTO_REGEX.match(instruction):
		instruction_type = encode_label(match.group("TARGET")) + 2
	# No match
	else:
		raise ValueError(f"Unrecognized instruction: {instruction}")
	# get a and c from the label and variable capture groups
	label = encode_label(match.group("LABEL"))
	variable = encode_var(match.group("VAR")) - 1
	return label, instruction_type, variable


def encode_instruction(instruction: str) -> int:
	"""Encodes a given instruction into a number"""
	a, b, c = convert_instruction(instruction)
	return encode_pair(a, encode_pair(b, c))


def encode_program_as_sequence(program: str) -> Generator[int, None, None]:
	"""Encodes a program into a sequence of numbers"""
	return (encode_instruction(instruction) for instruction in program.split("\n"))


def sequence_to_godel_number(sequence: Generator[int, None, None]) -> int:
	"""Converts a sequence of numbers into a Godel number"""
	product = 1
	for prime in prime_generator():
		try:
			product *= prime ** next(sequence)
		except StopIteration:
			break
	return product


def encode_program_as_number(program: str) -> int:
	"""Encodes a program into a program number"""
	trimmed_program = program.strip()
	if not trimmed_program:
		return 0
	return sequence_to_godel_number(encode_program_as_sequence(trimmed_program)) - 1
