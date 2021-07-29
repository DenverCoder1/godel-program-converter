from program_encoder import encode_program_as_number


if __name__ == "__main__":
	"""Given code in S language, print it's program number"""
	program = input("Enter program:\n")
	print(f"Program number: {encode_program_as_number(program)}")
