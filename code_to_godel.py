from program_encoder import encode_program_as_number


if __name__ == "__main__":
	"""Given code in S language, print it's program number"""
	print("Enter program (press enter twice to submit):")
	program = ""
	while True:
		code = input()
		program += code + "\n"
		if code == "":
			break
	print(f"Program number: {encode_program_as_number(program)}")
