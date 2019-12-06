from itertools import count


def main() -> None:
    target_row = 2981
    target_column = 3075

    nth_position = get_position(target_column, target_row)

    value = 20151125
    while nth_position > 1:
        value = (value * 252533) % 33554393
        nth_position -= 1

    print(value)


def get_column_start(column: int) -> int:
    total = 0
    while column > 0:
        total += column
        column -= 1

    return total


def get_position(column: int, row: int) -> int:
    position = get_column_start(column)
    counter = 1
    while counter < row:
        position += column + counter-1
        counter += 1

    return position


if __name__ == "__main__":
    main()
