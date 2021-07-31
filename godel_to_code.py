import sys

from decode_number import decode_number_as_code


def main():
	"""Given a program number, print the program it encodes"""
	try:
		# get the program number from the command line
		program_number = int(sys.argv[1])
	except IndexError:
		# prompt user for input
		program_number = int(input("Enter a program number: "))
	# decode the number and print the code
	print(decode_number_as_code(program_number))


if __name__ == "__main__":
	main()
