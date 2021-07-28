# godel-number-to-code

Program to convert a program encoding based on its Gödel number to 𝒮 Language (S Language)

## How to use

Launch the program with the following command:

`python3 godel-to-code.py`

(The command for Python may be different on your system.  See the [Python documentation](https://docs.python.org/3/using/index.html) for details.)

Enter a program number when prompted.

## Examples

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