from typing import Generator, List, Tuple

# generator for prime numbers
def prime_generator() -> Generator[int, None, None]:
    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 2


# check if a number is a prime number
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# calculate the sequence numbers given the godel number
def godel_number_to_sequence(godel_number: int) -> List[int]:
    code = []
    for prime in prime_generator():
        if godel_number <= 1:
            break
        instruction = 0
        while godel_number % prime == 0:
            instruction += 1
            godel_number = godel_number / prime
        code.append(instruction)
    return code


# encode a pair of numbers
def encode_pair(x: int, y: int) -> int:
    return 2 ** x * (2 * y + 1) - 1


# return left and right given a pair encoding
def get_left_right(pair_number: int) -> Tuple[int, int]:
    for x in range(pair_number + 1):
        for y in range(pair_number + 1):
            if encode_pair(x, y) == pair_number:
                return x, y


# get label from number
def get_label(label_number: int) -> str:
    if label_number == 0:
        return ""
    letter = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}[(label_number - 1) % 5]
    number = (label_number - 1) // 5 + 1
    return "[" + letter + str(number) + "] "


# get instruction type
def get_instruction_type(type: int) -> str:
    # branching
    if type > 2:
        return f"IF V≠0 GOTO {get_label(type - 2)}"
    # other instructions
    return {0: "V ← V", 1: "V ← V + 1", 2: "V ← V - 1"}[type]


# get variable name from number
def get_variable(variable_number: int) -> str:
    if variable_number == 1:
        return "Y"
    letter = "X" if variable_number % 2 == 0 else "Z"
    number = variable_number // 2
    return letter + str(number)


# translate instruction encoding to code
def translate_instruction(instruction_number: int) -> str:
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


# translate program encoding to code
def translate_program(program_number: int) -> str:
    godel_number = program_number + 1
    instructions = godel_number_to_sequence(godel_number)
    return "\n".join(translate_instruction(i) for i in instructions)


if __name__ == "__main__":
    program_number = int(input("Enter program number: "))
    print(translate_program(program_number))
