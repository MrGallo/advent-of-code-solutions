# Advent of Code Primer
[Advent of Code](https://adventofcode.com)

## Taking input
The majority of AOC questions come in the form of a text file called `input.txt`. The goal is to save that file to the same folder as your code so you can read in the data.

The data comes in various structures, and therefore may require a different approach to collection the data. Generally, you can count on reading the file with `with open()`. Please view my various solutions to get an idea of how to read in the data.

Things to know:
- [Reading from a file using `with open()`](https://github.com/MrGallo/classroom-examples/tree/master/08-file-rw#read-from-a-file)
- Creating and appending to a list.
- Using the string `.split()` method.
- Looping line by line with a for loop.
- Using the `strip()` method.

Handling:
- [Numbers on different lines](#numbers-on-different-lines)
- [Numbers separated by comma](#numbers-separated-by-comma)

## Numbers on different lines
Sometimes the input file will be a list of numbers each on a new line (see below). If this is the case, you have a couple options. 1) You can loop over the file, or 2) you can use `.split()`.

```
67931
140303
100800
69347
113036
127599
55139
99718
```

### Loop over the file
Loop over the file and append the contents to a new list:
```python
with open("input.txt", "r") as f:
    lines = []
    for line in f:
        lines.append(line)

# lines: ['67931\n', '140303\n', '100800\n', '69347\n', '113036\n', '127599\n', '55139\n', '99718']
```
Notice that the new line `\n` character is still there. To remove it, append `line.strip()`. This will remove all white-space from the beginning and the end of the string. One you strip the string, the list will still consist of strings. This input is supposed to be a list of numbers, so as you append, you need to use the `int()` function to convert the data to `int`.

### Use `.split`
```python
with open("input.txt", "r") as f:
    lines = f.read().split("\n")

# lines: ['67931', '140303', '100800', '69347', '113036', '127599', '55139', '99718']
```
Notice when you split, it doesn't include the split character in any of the strings. The list is still a list of strings, however. They need to be converted to `int`. Just set up a loop to go through the list, converting the strings to ints.
```python
int_list = []
for n in lines:
    int_list.append(int(n))
```
**or**
```python
for i, n in enumerate(lines):
    lines[i] = int(lines[i])
```
**or**
```python
with open("input.txt", "r") as f:
    lines = [int(n) for n in f.read().split("\n")]
```

## Numbers separated by comma
Some input files have numbers separated by commas, or spaces, or comma-spaces (`, `). In this case, split the string with whatever separates the numbers.
