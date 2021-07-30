from godel_utils import decode_pair, godel_number_to_sequence


def get_label(label_number: int) -> str:
	"""
	Get label from number

	If the number is 0, there is no label.

	Othewise, the number is the index in the sequence:

	```
	A1, B1, C1, D1, E1, A2, B2, C2, ...
	```
	"""
	if label_number == 0:
		return ""
	# get a letter A-E based on the modulo being 0-5 respectively
	letter = chr((label_number - 1) % 5 + ord("A"))
	# get the index number of the label
	number = (label_number - 1) // 5 + 1
	# wrap label in brackets
	return "[" + letter + str(number) + "] "


def get_instruction_type(type: int) -> str:
	"""
	Get instruction type from number

	- type = 0: NOOP
	- type = 1: ADD
	- type = 2: SUB
	- type > 2: GOTO with target label having #(L) = type - 2
	"""
	# branching
	if type > 2:
		return f"IF V≠0 GOTO {get_label(type - 2)}"
	# other instructions
	return {0: "V ← V", 1: "V ← V + 1", 2: "V ← V - 1"}[type]


def get_variable(variable_number: int) -> str:
	"""
	Get variable name from its number

	Variable numbers represent the index in the following sequence:
	```
	Y, X1, Z1, X2, Z2, X3, Z3, ...
	```
	"""
	# return "Y" if the number is 1
	if variable_number == 1:
		return "Y"
	# X if even index, Z if odd index
	letter = "X" if variable_number % 2 == 0 else "Z"
	# index number of the variable
	number = variable_number // 2
	# return the variable name
	return letter + str(number)


def translate_instruction(instruction_number: int) -> str:
	"""Translate an instruction number to code"""
	code = ""
	# split the encoded pairs
	# a represents the label of the instruction
	# b represents the type of instruction
	# c represents the variable of the instruction
	a, bc = decode_pair(instruction_number)
	b, c = decode_pair(bc)
	# translate the label
	code += get_label(a)
	# translate the instruction type
	code += get_instruction_type(b)
	# replace all occurrences the variable
	code = code.replace("V", get_variable(c + 1))
	# return the translated instruction
	return code


def translate_program(program_number: int) -> str:
	"""
	Translate program number to code

	First, 1 is added to the program number to get the Gödel number

	The Gödel number is then translated to a sequence of instructions

	Each instruction is then translated to code
	"""
	godel_number = program_number + 1
	# get the sequence of instruction numbers
	instructions = godel_number_to_sequence(godel_number)
	# translate each instruction and join the code
	return "\n".join(translate_instruction(i) for i in instructions)
