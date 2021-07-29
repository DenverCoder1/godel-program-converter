import re
from typing import Generator, Tuple

from primes import prime_generator
from godel_utils import encode_pair

# NOOP - groups: LABEL, VAR
NOOP_REGEX = re.compile(
	r"^\s*(?:\[(?P<LABEL>[A-E]\d*)\])?\s*(?P<VAR>(Y|[XZ]\d*))\s*(?:←|<-?|<?=)\s*(?P=VAR)\s*$"
)

# ADD - groups: LABEL, VAR
ADD_REGEX = re.compile(
	r"^\s*(?:\[(?P<LABEL>[A-E]\d*)\])?\s*(?P<VAR>(Y|[XZ]\d*))\s*(?:←|<-?|<?=)\s*(?P=VAR)\s*[+]\s*1\s*$"
)

# MINUS - groups: LABEL, VAR
MINUS_REGEX = re.compile(
	r"^\s*(?:\[(?P<LABEL>[A-E]\d*)\])?\s*(?P<VAR>(Y|[XZ]\d*))\s*(?:←|<-?|<?=)\s*(?P=VAR)\s*[-∸−]\s*1\s*$"
)

# GOTO - groups: LABEL, VAR, TARGET
GOTO_REGEX = re.compile(
	r"^\s*(?:\[(?P<LABEL>[A-E]\d*)\])?\s*(?:IF|If|if)\s+(?P<VAR>(Y|[XZ]\d*))\s*(?:≠|!=|=/=)\s*[0],?\s+GOTO\s+(?P<TARGET>[A-E]\d*)\s*$"
)


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
	match = NOOP_REGEX.match(instruction)
	if match:
		return encode_label(match.group("LABEL")), 0, encode_var(match.group("VAR")) - 1
	# ADD
	match = ADD_REGEX.match(instruction)
	if match:
		return encode_label(match.group("LABEL")), 1, encode_var(match.group("VAR")) - 1
	# MINUS
	match = MINUS_REGEX.match(instruction)
	if match:
		return encode_label(match.group("LABEL")), 2, encode_var(match.group("VAR")) - 1
	# GOTO
	match = GOTO_REGEX.match(instruction)
	if match:
		return (
			encode_label(match.group("LABEL")),
			encode_label(match.group("TARGET")) + 2,
			encode_var(match.group("VAR")) - 1,
		)
	raise ValueError(f"Unrecognized instruction: {instruction}")


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
