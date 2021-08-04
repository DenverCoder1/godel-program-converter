from typing import Generator, Tuple

from src.godel_utils import encode_pair, sequence_to_godel_number

from .constants import ADD_REGEX, GOTO_REGEX, MINUS_REGEX, NOOP_REGEX


def encode_label(label: str) -> int:
	"""
	Encodes a label into a number

	If there is no label, the number is 0.

	Othewise, the number is the index in the sequence:

	```
	A1, B1, C1, D1, E1, A2, B2, C2, ...
	```

	A, B, C, D, E are interpretted as A1, B1, C1, D1, E1, respectively.
	"""
	if not label:
		return 0
	# part after letter if it has a number, otherwise 1
	index = int(label[1:]) if len(label) > 1 else 1
	# A = 1, B = 2, ... E = 5
	offset = ord(label[0]) - ord("A") + 1
	# compute label number
	return (index - 1) * 5 + offset


def encode_var(variable: str) -> int:
	"""
	Encodes a label into a number

	Returns the index of the variable in the sequence:

	```
	Y, X1, Z1, X2, Z2, X3, Z3, ...
	```

	X and Z are interpretted as X1 and Z1, respectively.
	"""
	if variable == "Y":
		return 1
	index = int(variable[1:]) if len(variable) > 1 else 1
	offset = {"X": 0, "Z": 1}[variable[0]]
	return index * 2 + offset


def convert_instruction(instruction: str) -> Tuple[int, int, int]:
	"""
	Determine the a, b, and c values for a given instruction as a string

	a = 0 for unlabeled instructions, otherwise a = #(L) where L is the instruction label

	b represents the type of instruction:

	- NOOP: b = 0
	- ADD: b = 1
	- SUB: b = 2
	- GOTO: b = #(L) + 2 where L is the target label

	c = #(V) - 1 where V is the variable in the instruction
	"""
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
	"""
	Encodes a given instruction into a number

	An instruction number is the pair encoding of `<a, <b, c>>` where `a` represents
	the label, `b` represents the instruction type, and `c` represents the variable
	"""
	a, b, c = convert_instruction(instruction)
	return encode_pair(a, encode_pair(b, c))


def encode_program_as_sequence(program: str) -> Generator[int, None, None]:
	"""
	Encodes a program into a sequence of numbers

	Each instruction is encoded into a number and yielded
	"""
	instructions = program.split("\n")
	# yield each instruction number for every non-empty line
	return (encode_instruction(i) for i in instructions if i != "")


def encode_program_as_number(program: str) -> int:
	"""
	Encodes a program into a program number

	First, the program is encoded as a sequence of instruction numbers
	Then, the sequence is converted into a program number using its Gödel number - 1
	"""
	return sequence_to_godel_number(encode_program_as_sequence(program)) - 1
