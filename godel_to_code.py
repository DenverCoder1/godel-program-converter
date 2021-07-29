from code_writer import translate_program


if __name__ == "__main__":
	"""Given a program number, print the program it encodes"""
	program_number = int(input("Enter program number: "))
	print(translate_program(program_number))
