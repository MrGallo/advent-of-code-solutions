# Advent of Code - Beginner Edition

The Advent of Code, while extremely fun, is also extremely difficult for begninners and even some intermediate programmers. I will try my best to keep up with the days and distill the problem in to more manageable chunks.

| | | | | |
| - | - | - | - | - |
| [Day 1](#day-1) | [Day 2](#day-2) | [Day 3](#day-3) |  |  |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


## Day 1
Check out the original [Day 1](https://adventofcode.com/2023/day/1) problem.

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

## Day 2
Check out the original [Day 2](https://adventofcode.com/2023/day/2) problem.

You meet an elf playing a game, drawing many red, green and blue cubes out of a bag.

1.  You need to be able to take a single draw and determine how many cubes of each color were drawn. You need to take a string like `"3 green, 15 blue, 14 red"` and output the amounts on separate lines.
2. Not every draw will contain all three colors and the colors will not always be listed in the same order. Your program should take that into account. For example it should work with both strings shown here:
    ```
    3 green, 15 blue, 14 red
    2 red, 5 green
    ```
3. Additionally each game consists of many draws, separated by a semi-colon (`;`). Here are some games:
    ```
    3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    ```
4. Determine if any particular game is possible if you only have the following amounts of colored cubes:
    ```
    red - 12
    blue - 13
    green - 14
    ```
    In #3, the only possible games would be games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once.
5. Rather than determine if the game would be possible with a limited number of cubes, figure out the least amount of each colour a single game would require to be possible. For example `3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green` would require `4 red 2 green 6 blue` in order for this game to be possible.


## Day 3
Check out the [original problem](https://adventofcode.com/2023/day/3).

You have to repair a gondola (a suspended cart to get up a mountain). The elves give you a schematic for the machine. You need to find all the numbers next to a symbol.

1. Given a string, find all the numbers beside a "*" symbol. These are referred to as 'part numbers' on the schematic. What is the sum of all the part numbers? Here is an example:
    ```
    "..4.*3...7*5." -> 3 + 7 + 5 = 15
    ```
    4 is not considered a part because it is not beside a `*`.
2. Given a list of these strings make up an entire schematic diagram.
    ```
    ..7....4..
    ...*......
    ..3...6...
    ......*...
    ..7*......
    ```
    Now you need to count numbers next to `*` even above, below and diagonally. What is the sum of all the numbers that are parts? In this example, the sum is `7 + 3 + 7 + 6 = 23` ( the `4` is the only one not adjacent to a star)
3. Stars that are beside *exactly* two numbers are gears. For every star that is a gear, multiply the two numbers together to get the "gear ratio". Add these all the gear ratios together.

