from collections import Counter
from typing import List, Tuple
import re


def main() -> None:
    with open("input.txt", "r") as f:
        rooms = f.read().split("\n")

    print(part1(rooms))  # answer: 245102
    print(part2(rooms))  # answer: 324


def part1(rooms: List[str]) -> int:
    real_room_ids = []
    for room in rooms:
        encrypted_name, sector_id, checksum = parse_encrypted_room(room)
        valid_checksum = generate_checksum(encrypted_name)
        if valid_checksum == checksum:
            real_room_ids.append(sector_id)

    return sum(real_room_ids)


def part2(rooms: List[str]) -> int:
    for room in rooms:
        encrypted_name, sector_id, checksum = parse_encrypted_room(room)
        decrypted_name = decrypt_name(encrypted_name, sector_id)
        if "north" in decrypted_name:
            print(decrypted_name)
            return sector_id


def decrypt_name(name: str, sector_id: int) -> str:
    decrypted_name = ""
    for encoded_char in name:
        if encoded_char == "-":
            decoded_char = " "
        else:
            decoded_char = chr((ord(encoded_char) - 97 + sector_id) % 26 + 97)

        decrypted_name += decoded_char
    return decrypted_name


def parse_encrypted_room(room: str) -> Tuple:
    regex = r"([a-z\-]+)-([0-9]+)\[(.+)\]$"
    matches = re.search(regex, room)
    name = matches.group(1)
    sector_id = int(matches.group(2))
    checksum = matches.group(3)
    return name, sector_id, checksum


def generate_checksum(room_name: str) -> str:
    count = Counter(room_name.replace("-", ""))
    most_common = sorted(count.most_common(), key=occurance_alpha, reverse=True)
    return "".join([l for l, c in most_common])[:5]


def occurance_alpha(a: Tuple):
    a_letter, a_count = a
    return a_count, -ord(a_letter)


if __name__ == "__main__":
    main()
