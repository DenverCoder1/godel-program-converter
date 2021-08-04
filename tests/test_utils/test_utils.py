import os
from typing import Generator


def read_program(filename: str) -> str:
	"""Read program from file"""
	filepath = os.path.dirname(__file__)
	with open(os.path.join(filepath, "..", "programs", filename), "r") as f:
		return f.read()


def gen(*args: int) -> Generator[int, None, None]:
	"""Convert arguments to generator"""
	return (_ for _ in args)
