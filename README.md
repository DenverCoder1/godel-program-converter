# Gödel Program Converter

Program to convert a program encoding based on its Gödel number to 𝒮 Language (S Language) or convert an 𝒮 Language program to its program number

- [Convert a program number to code](#convert-a-program-number-to-code)
  - [Running the code](#running-the-code)
  - [Examples](#examples)
- [Convert code to a program number](#convert-code-to-a-program-number)
  - [Running the code](#running-the-code-1)
  - [How to input code](#how-to-input-code)
  - [Examples](#examples-1)
- [See also](#see-also)

## Convert a program number to code

### Running the code

#### Method 1: Command line input

Launch the program, providing the number as a command line argument:

`python3 godel_to_code.py [program number]`

For example: `python3 godel_to_code.py 52`

(The command for Python may be different on your system.  See the [Python documentation](https://docs.python.org/3/using/index.html) for details.)

#### Method 2: Interactive input

Launch the program with the following command:

`python3 code_to_godel.py`

Enter a program number when prompted.

### Examples

```
Enter program number: 99
Y ← Y + 1
Y ← Y
Y ← Y + 1
```

```
Enter program number: 25724
Y ← Y
[A1] Y ← Y
Y ← Y + 1
[B1] Y ← Y
```

```
Enter program number: 2097151
[A1] X1 ← X1 + 1
```

## Convert code to a program number

### Running the code

#### Method 1: File input

Launch the program with the following command:

`python3 code_to_godel.py test.s`

Where `test.s` is the name of the file containing the program.

#### Method 2: Command line input

Launch the program with the code input as a command line argument:

Single line:

`python3 code_to_godel.py "Y <- Y + 1"`

Multiline:

```
python3 code_to_godel.py <<EOF
Y <- Y
Y <- Y + 1
```

#### Method 3: Interactive input

Launch the program with the following command:

`python3 code_to_godel.py`

Enter the code line by line when prompted. Enter a blank line to end the input.

### How to input code

* Assignment can be represented by `<-`, `=`, `<=` or `←`.
* Inequality can be represented by `!=`, `=/=`, or `≠`.
* Labels must only contain indexed letters A-E, and variables must be either `Y`, or an indexed `X` or `Z`.
* Labels without indices will be interpreted as index 1 (eg. `[A]` is equivalent to `[A1]`).
* Variables without indices will be interpreted as index 1 (eg. `X` is equivalent to `X1`).
* Valid instructions include: `V ← V`, `V ← V + 1`, `V ← V - 1`, and `IF V≠0 GOTO L` where in all cases, `V` represents a variable and `L` represents a label as specified above.
* Instructions can be preceded by a label in square brackets (eg. `[A]`).

### Examples

```
Enter program (press enter twice to submit):

Program number: 0
```

```
Enter program (press enter twice to submit):
Y <- Y                       
[A] Y <- Y
Y <- Y + 1
[B] Y <- Y

Program number: 25724
```

```
Enter program (press enter twice to submit):
IF X != 0 GOTO A 
Y <- Y + 1
[A1] Y <- Y - 1    

Program number: 773094113279999999999999
```

## See also

  * [S-interpreter](https://github.com/abrahammurciano/s-interpreter) by [@abrahammurciano](https://github.com/abrahammurciano)

