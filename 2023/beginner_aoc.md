# Advent of Code - Beginner Edition

The Advent of Code, while extremely fun, is also extremely difficult for begninners and even some intermediate programmers. I will try my best to keep up with the days and distill the problem in to more manageable chunks.

## Day 1
1. Given a string containing letters and numbers, extract the first and last number and stick them together. For example given the string `"ab4c5d9ef"`, your program would output the integer `49`. Reason: `4` is the first number in the string and `9` is the last. Use `string.isdigit()` to determine if a particular character is a number.
    ```python
    # tests
    "ab4c5d9ef" -> 49
    "a1b" -> 11
    "3xy5" -> 35
    ```
2. Given a list of such strings as described in #1, calculate the sum of all the numbers.
    ```python
    # test
    strings = [
        "ab4c5d9ef",   # 49
        "a1b",         # 11
        "3xy5",        # 35
    ]

    # total would be 95 when you add all their numbers together
    ```
3. Some strings will have the words `"one" "two" "three" "four" "five" "six" "seven" "eight" and "nine"`. These need to also be considered numbers in the strings. For example:
    ```python
    "one3two" -> 12
    "twone"   -> 21
    "oneightwone" -> 11  # should be discovering 1821 in that string as numbers
    ```
    ```python
    # Test
    strings = [
        "ab4c5d9ef",   # 49
        "a1b",         # 11
        "3xy5",        # 35
        "one3two",     # 12
        "twone",       # 21
        "oneightwone"  # 11
    ]

    # total should be 139
    ```
