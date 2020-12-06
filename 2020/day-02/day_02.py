from typing import List, Tuple, Callable

Password = Tuple[str, str, int, int]


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().split("\n")

    passwords = []
    for line in lines:
        password = line.split()[-1]  # last 'word'
        colon_pos = line.index(':')
        minmax, letter = line[:colon_pos].split()
        a, b = map(int, minmax.split("-"))
        passwords.append((password, letter, a, b))
    
    print(len(valid_passwords(passwords, is_valid_sled_rental_password)))  # Part 1: 628
    print(len(valid_passwords(passwords, is_valid_toboggan_rental_password)))  # Part 2: 705


def valid_passwords(passwords: List[Password], validation_func: Callable) -> List[Password]:
    return [password for password in passwords if validation_func(password)]


def is_valid_sled_rental_password(password: Password) -> bool:
    text, letter, low, high = password
    count = text.count(letter)
    return count >= low and count <= high


def is_valid_toboggan_rental_password(password: Password) -> bool:
    text, letter, a, b = password
    in_pos_one = text[a-1] == letter
    in_pos_two = text[b-1] == letter
    return in_pos_one and not in_pos_two or in_pos_two and not in_pos_one


if __name__ == "__main__":
    main()
