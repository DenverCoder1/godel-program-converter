from program_encoder import encode_program_as_number


if __name__ == "__main__":
	"""Given code in S language, print its program number"""
	print("Enter program (press enter twice to submit):")
	program = ""
	# read lines of input into program until and empty line is entered
	while True:
		code = input()
		program += code + "\n"
		if code == "":
			break
	# encode program as number
	print(f"Program number: {encode_program_as_number(program)}")
