from src.decode_number.decode_number import (
	decode_number_as_code,
	translate_label,
	translate_line_label,
	translate_instruction_type,
	translate_variable,
	translate_instruction,
)

from .test_utils.constants import BASIC, GOTO, VARIABLES
from .test_utils.test_utils import read_program


def test_decode_basic():
	"""Create program with NOOP, ADD, MONUS from program number"""
	program_number = BASIC
	# expected program
	expected_program = read_program("test_basic.s")
	# decode program
	assert expected_program == decode_number_as_code(program_number)


def test_decode_goto():
	"""Create program with GOTO from program number"""
	program_number = GOTO
	# expected program
	expected_program = read_program("test_goto.s")
	# decode program
	assert expected_program == decode_number_as_code(program_number)


def test_decode_variables():
	"""Create program with VARIABLES from program number"""
	program_number = VARIABLES
	# expected program
	expected_program = read_program("test_variables.s")
	# decode program
	assert expected_program == decode_number_as_code(program_number)


def test_translate_label():
	"""Test decoding of label number"""
	assert translate_label(0) == ""
	assert translate_label(1) == "A1"
	assert translate_label(5) == "E1"
	assert translate_label(35) == "E7"
	assert translate_label(50) == "E10"


def test_translate_line_label():
	"""Test translation of line labels"""
	assert translate_line_label(0) == ""
	assert translate_line_label(50) == "[E10] "


def test_translate_instruction_type():
	"""Test translation of instruction types"""
	assert translate_instruction_type(0) == "V ← V"
	assert translate_instruction_type(1) == "V ← V + 1"
	assert translate_instruction_type(2) == "V ← V - 1"
	assert translate_instruction_type(3) == "IF V≠0 GOTO A1"


def test_translate_variable():
	"""Test translation of variables"""
	assert translate_variable(1) == "Y"
	assert translate_variable(2) == "X1"
	assert translate_variable(3) == "Z1"
	assert translate_variable(15) == "Z7"
	assert translate_variable(21) == "Z10"


def test_translate_instruction():
	"""Test translation of instructions"""
	assert translate_instruction(0) == "Y ← Y"
	assert translate_instruction(1) == "[A1] Y ← Y"
	assert translate_instruction(2) == "Y ← Y + 1"
