

def main() -> None:
    with open("input.txt", "r") as f:
        compressed_string = f.read()

    # part 1
    decompressed = decompress(compressed_string)
    print(len(decompressed))  # answer: 110346

    # part 2
    length = get_decompress_v2_length(compressed_string)
    print(length)  # answer: 10774309173


def decompress(string: str) -> str:
    if string == "":
        return ""

    if string[0] == "(":
        i = string.find("x")
        end = string.find(")")
        n = int(string[1:i])
        times = int(string[i+1:end])
        return string[end+1:end+1+n] * times + decompress(string[end+1+n:])
    return string[0] + decompress(string[1:])


def get_decompress_v2_length(string: str) -> int:
    if len(string) == 0:
        return 0

    if string[0] == "(":
        x = string.find("x")
        end = string.find(")")
        n = int(string[1:x])
        times = int(string[x+1:end])
        return (get_decompress_v2_length(string[end+1:end+1+n]) * times
                + get_decompress_v2_length(string[end+1+n:]))
    else:
        return 1 + get_decompress_v2_length(string[1:])


if __name__ == "__main__":
    main()
