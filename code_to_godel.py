import sys
import os

from program_encoder import encode_program_as_number


def read_program() -> str:
	"""
	Check for the input code.
	If the argument is not a file, then it will be treated as input code.
	If no argument is given, then the user will be prompted to enter the code.
	"""
	# check if an argument was passed
	if len(sys.argv) > 1:
		# check if the argument is a file
		if os.path.isfile(sys.argv[1]):
			with open(sys.argv[1], "r") as f:
				return f.read()
		# treat argument as a string
		return sys.argv[1]
	# prompt user for input
	print("Enter program (press enter twice to submit):")
	program = ""
	# read lines of input into program until and empty line is entered
	while line := input():
		program += line + "\n"
	return program


def main():
	"""Given code in S language, print its program number"""
	# read input program
	program = read_program()
	# encode program as number
	print(f"Program number: {encode_program_as_number(program)}")


if __name__ == "__main__":
	main()
