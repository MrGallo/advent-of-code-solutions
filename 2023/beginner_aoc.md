# Advent of Code - Beginner Edition

The Advent of Code, while extremely fun, is also extremely difficult for begninners and even some intermediate programmers. I will try my best to keep up with the days and distill the problem in to more manageable chunks.

| | | | | |
| - | - | - | - | - |
| [Day 1](#day-1) | [Day 2](#day-2) | [Day 3](#day-3) | [Day 4](#day-4) | [Day 5](#day-5) |
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

## Day 4
Check out the [original problem](https://adventofcode.com/2023/day/4).

The goal is to check lottery cards to see how many correct numbers were selected. Here are some examples of lottery cards:
```
"41 48 83 86 17 | 83 86  6 31 17  9 48 53"
"13 32 20 16 61 | 61 30 68 82 17 32 24 19"
" 1 21 53 59 44 | 69 82 63 72 16 21 14  1"
```
The winning numbers are on the left and what you picked is on the right.

1. Given a single lottery card like `"41 48 83 86 17 | 83 86  6 31 17  9 48 53"`. Split the card into the two sides (left and right). 
2. Create two lists of integers from the split up card.
3. Figure out how many of your picks (on the right) match the winning numbers (on the left).
4. How many winning numbers are there for all the cards combined below? You need to start with this list and use a loop to iterate through all the cards. This should work for any number of cards with any numbers.
    ```
    cards = [
        "41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        " 1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    ]
    ```

## Day 5
Check out the [original problem](https://adventofcode.com/2023/day/5).

You have a list of types of seeds and you need to be able to determine what location of land they should be planted in.

1. Given some seed numbers in a string separated by space, read them into a list as integers. The string is `"79 14 55 13"`.
2. Each seed has a specific location but the seed number needs to be mapped to a location. Here is the map:
    ```
    60 56 37
    56 93 4
    ```
    These two lines represent two ranges each. On each line, the first number is the resulting **location start**, the second number is the **seed number start**, the third number is the **amount of numbers** in each range. So in the first line the location range is `60 + 37`, which gives us locations `60` to `96` *inclusive*. The seed range means any seeds with numbers `56` to `92` *inclusive* will be changed to the particular location range. So, a seed number of `56` will be mapped to location `60`, seed number `57` will be mapped to location `61`, `58 -> 62`, `59 -> 63` and so on. Seed numbers that don't get mapped to a new location will just be planted at the number that thay are, so a seed number of `50` (which is out of any of the ranges) will just be planted at location `50`.

    What location should each seed be planted at?
3. The twist of the original question is the original seed numbers are actually ranges of seeds you have. The first number is where the seed number starts and the next number is how many seeds in the range, so the first pair of numbers `79` and `14`, really means you have seeds 79, 80, 81, ... 92 *inclusive*. Which is starting at `79` and consisting of `14` different seeds. Now find the lowest location that can be planted at given the seeds you have.