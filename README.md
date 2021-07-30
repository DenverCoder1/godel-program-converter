# godel-program-converter

Program to convert a program encoding based on its Gödel number to 𝒮 Language (S Language) or convert an 𝒮 Language program to its program number

- [Convert a program number to code](#convert-a-program-number-to-code)
  - [Examples](#examples)
- [Convert code to a program number](#convert-code-to-a-program-number)
  - [Examples](#examples-1)
- [See also](#see-also)

## Convert a program number to code

Launch the program with the following command:

`python3 godel_to_code.py`

(The command for Python may be different on your system.  See the [Python documentation](https://docs.python.org/3/using/index.html) for details.)

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

Launch the program with the following command:

`python3 code_to_godel.py`

Enter the code line by line when prompted. Enter a blank line to end the input.

Note:

* Assignment can be represented by `<-`, `=`, `<=` or `←`.
* Inequality can be represented by `!=`, `=/=`, or `≠`.
* Labels must only contain indexed letters A-E, and variables must be either `Y`, or an indexed X or Z.
* Labels without indices will be interpreted as index 1 (eg. `[A]` is equivalent to `[A1]`).
* Variables without indices will be interpreted as index 1 (eg. `X` is equivalent to `X1`).

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
[A] Y <- Y - 1    

Program number: 773094113279999999999999
```

## See also

  * [S-interpreter](https://github.com/abrahammurciano/s-interpreter) by https://github.com/abrahammurciano

