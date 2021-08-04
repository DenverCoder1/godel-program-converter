from src.encode_program import (
	encode_program_as_number,
	encode_label,
	encode_var,
	convert_instruction,
)

from .test_utils.constants import BASIC, GOTO, VARIABLES
from .test_utils.test_utils import read_program

import pytest


def test_encode_program_basic():
	"""Encode program with NOOP, ADD, MONUS to program number"""
	# read input program
	program = read_program("test_basic.s")
	# encode program as number
	assert encode_program_as_number(program) == BASIC


def test_encode_program_goto():
	"""Encode program with GOTO to program number"""
	# read input program
	program = read_program("test_goto.s")
	# encode program as number
	assert encode_program_as_number(program) == GOTO


def test_encode_program_assignment():
	"""Encode program with alternate assignment operators"""
	# read input program
	program = read_program("test_assignment.s")
	# encode program as number
	assert encode_program_as_number(program) == BASIC


def test_encode_program_inequality():
	"""Encode program with alternate inequality operators"""
	# read input program
	program = read_program("test_inequality.s")
	# encode program as number
	assert encode_program_as_number(program) == GOTO


def test_encode_program_short_label():
	"""Encode program with implicit index for labels"""
	# read input program
	program = read_program("test_short_label.s")
	# encode program as number
	assert encode_program_as_number(program) == GOTO


def test_encode_program_variables():
	"""Encode program with variables"""
	# read input program
	program = read_program("test_variables.s")
	# encode program as number
	assert encode_program_as_number(program) == VARIABLES


def test_encode_program_short_variables():
	"""Encode program with variables"""
	# read input program
	program = read_program("test_short_variables.s")
	# encode program as number
	assert encode_program_as_number(program) == VARIABLES


def test_encode_label():
	"""Test translation of labels"""
	assert encode_label(None) == 0
	assert encode_label("A") == 1
	assert encode_label("A1") == 1
	assert encode_label("E") == 5
	assert encode_label("E7") == 35
	assert encode_label("E10") == 50


def test_encode_var():
	"""Test translation of variables"""
	assert encode_var("Y") == 1
	assert encode_var("X") == 2
	assert encode_var("X1") == 2
	assert encode_var("Z") == 3
	assert encode_var("Z7") == 15
	assert encode_var("Z10") == 21


def test_convert_instruction():
	"""Test translation of instructions"""
	assert convert_instruction("Y <- Y") == (0, 0, 0)
	assert convert_instruction("X <- X") == (0, 0, 1)
	assert convert_instruction("Y <- Y + 1") == (0, 1, 0)
	assert convert_instruction("Y <- Y - 1") == (0, 2, 0)
	assert convert_instruction("[A] Y <- Y") == (1, 0, 0)
	assert convert_instruction("IF Y != 0 GOTO A") == (0, 3, 0)


def test_convert_instruction_invalid():
	"""Test translation of instructions with invalid instructions"""
	# test invalid operator
	with pytest.raises(ValueError):
		convert_instruction("Y <- Y * 1")
	# test mismatched variables
	with pytest.raises(ValueError):
		convert_instruction("Y <- X")
	# test invalid line label
	with pytest.raises(ValueError):
		convert_instruction("[F1] Y <- Y")
	# test invalid target label
	with pytest.raises(ValueError):
		convert_instruction("IF Y != 0 GOTO F1")
	# test invalid variable
	with pytest.raises(ValueError):
		convert_instruction("Y2 <- Y2")
