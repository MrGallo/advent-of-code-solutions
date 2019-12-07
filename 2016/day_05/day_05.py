import hashlib


def main() -> None:
    with open("input.txt", "r") as f:
        door_id = f.read().strip()

    print(part1(door_id))  # answer: 801b56a7
    print(part2(door_id))  # answer: 424a0197


def part1(door_id: str) -> str:
    i = 0
    password = ""
    print(password + "*" * (8-len(password)))
    while len(password) != 8:
        door_hash = hashlib.md5(bytes(door_id + str(i), 'utf-8')).hexdigest()
        if door_hash.startswith("00000"):
            password += door_hash[5]
            print(password + "*" * (8-len(password)))
        i += 1
    return password


def part2(door_id: str) -> str:
    i = 0
    password = list("*" * 8)
    print("".join(password))
    while "*" in password:
        door_hash = hashlib.md5(bytes(door_id + str(i), 'utf-8')).hexdigest()
        if door_hash.startswith("00000"):
            try:
                position = int(door_hash[5])
            except ValueError:
                i += 1
                continue
            character = door_hash[6]
            if position >= 0 and position < 8 and password[position] == "*":
                password[position] = character
                print("".join(password))
        i += 1
    return "".join(password)


if __name__ == "__main__":
    main()
