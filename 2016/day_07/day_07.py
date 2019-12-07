from typing import List, Tuple, Union
import re


def main() -> None:
    with open("input.txt", "r") as f:
        ips = f.read().split()

    print(part1(ips))  # answer: 115
    print(part2(ips))  # answer: 231


def part1(ips: List[str]) -> int:
    return len([ip for ip in ips if supports_tls(ip)])


def part2(ips: List[str]) -> int:
    return len([ip for ip in ips if supports_ssl(ip)])


def parse_ipv7(ip: str) -> Tuple[Tuple[str], Tuple[str]]:
    regex = r"\[(.+?)\]"
    supernet_sections = re.sub(regex, " ", ip, 0).split()
    hypernet_sections = re.findall(regex, ip)
    return (supernet_sections, hypernet_sections)


def supports_tls(ip: str) -> bool:
    supernet_sections, hypernet_sections = parse_ipv7(ip)
    for hypernet in hypernet_sections:
        if has_abba_pattern(hypernet):
            return False

    for string in supernet_sections:
        if has_abba_pattern(string):
            return True

    return False


def supports_ssl(ip: str) -> bool:
    supernet_sections, hypernet_sections = parse_ipv7(ip)
    for hypernet in hypernet_sections:
        for a, b, _ in get_aba_pattern(hypernet):
            for supernet in supernet_sections:
                if b+a+b in supernet:
                    return True
    return False


def has_abba_pattern(string: str) -> bool:
    i = 0
    while i < len(string) - 3:
        c1, c2, c3, c4 = string[i:i+4]
        if c1 == c4 and c2 == c3 and c1 != c2:
            return True
        i += 1
    return False


def get_aba_pattern(string: str) -> Tuple[str]:
    i = 0
    while i < len(string) - 2:
        c1, c2, c3 = string[i:i+3]
        if c1 == c3 and c1 != c2:
            yield c1, c2, c3
        i += 1


if __name__ == "__main__":
    main()
