import os
import sys

def create_files(year, day_number):
    day_number = str(day_number).zfill(2)
    folder_name = f"{year}/day_{day_number}"

    # Create the folder if it doesn't exist
    os.makedirs(folder_name, exist_ok=True)

    # Create the three files
    a = f'day_{day_number}.py'
    b = 'input.txt'
    c = 'test.txt'
    with open(os.path.join(folder_name, a), 'w') as file_a:
        file_a.write("# This is a.py\n")

    with open(os.path.join(folder_name, b), 'w') as file_b:
        file_b.write("# This is b.txt\n")

    with open(os.path.join(folder_name, c), 'w') as file_c:
        file_c.write("# This is c.txt\n")

    os.system(f"cd {folder_name}")
    os.system(f"code {a} {b} {c}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <year> <day_number>")
        sys.exit(1)

    year = sys.argv[1]
    day_number = sys.argv[2]

    create_files(year, day_number)
    print(f"Files created in {year}/day_{day_number}")
