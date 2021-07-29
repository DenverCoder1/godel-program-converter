from godel_utils import get_left_right, godel_number_to_sequence


def get_label(label_number: int) -> str:
	"""get label from number"""
	if label_number == 0:
		return ""
	letter = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}[(label_number - 1) % 5]
	number = (label_number - 1) // 5 + 1
	return "[" + letter + str(number) + "] "


def get_instruction_type(type: int) -> str:
	"""get instruction type from number"""
	# branching
	if type > 2:
		return f"IF V≠0 GOTO {get_label(type - 2)}"
	# other instructions
	return {0: "V ← V", 1: "V ← V + 1", 2: "V ← V - 1"}[type]


def get_variable(variable_number: int) -> str:
	"""get variable name from number"""
	if variable_number == 1:
		return "Y"
	letter = "X" if variable_number % 2 == 0 else "Z"
	number = variable_number // 2
	return letter + str(number)


def translate_instruction(instruction_number: int) -> str:
	"""translate instruction number to code"""
	code = ""
	a, bc = get_left_right(instruction_number)
	b, c = get_left_right(bc)
	# translate label
	code += get_label(a)
	# translate instruction type
	code += get_instruction_type(b)
	# replace all occurrences variable
	code = code.replace("V", get_variable(c + 1))
	return code


def translate_program(program_number: int) -> str:
	"""translate program number to code"""
	godel_number = program_number + 1
	instructions = godel_number_to_sequence(godel_number)
	return "\n".join(translate_instruction(i) for i in instructions)
