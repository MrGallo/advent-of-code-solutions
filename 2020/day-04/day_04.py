from typing import Dict, List

Document = Dict[str, str]


def main():
    with open('input.txt', 'r') as f:
        documents = [
            dict([pairs.split(":") for pairs in doc.replace("\n", " ").split()])
            for doc in f.read().split("\n\n")
        ]
    
    north_pole_credentials = get_north_pole_credentials(documents)
    print(len(north_pole_credentials))  # Part 1: 216

    valid_np_credentials = filter_out_invalid(north_pole_credentials)
    print(len(valid_np_credentials))  # Part 2: 150


def get_north_pole_credentials(documents: List[Document]) -> List[Document]:
    return [doc for doc in documents if is_north_pole_credential(doc)]


def is_north_pole_credential(document: Document) -> bool:
    required_data_set = set("byr iyr eyr hgt hcl ecl pid".split())
    data_set = set(document.keys())
    return required_data_set <= data_set


def filter_out_invalid(documents: List[Document]) -> List[Document]:
   return [doc for doc in documents if has_valid_data(doc)]


def has_valid_data(document: Document) -> bool:
    byr = int(document["byr"])
    iyr = int(document["iyr"])
    eyr = int(document["eyr"])
    hgt_str = document["hgt"]
    try:
        hgt, hgt_unit = int(hgt_str[:-2]), hgt_str[-2:]
    except ValueError:
        valid_hgt = False
    else:
        if hgt_unit == "cm":
            valid_hgt = hgt >= 150 and hgt <= 193
        elif hgt_unit == "in":
            valid_hgt = hgt >= 59 and hgt <= 76
        else:
            valid_hgt = False
    
    hcl_str = document["hcl"][1:]
    
    if len(hcl_str) == 6:
        try:
            hcl = int(hcl_str, 16)
        except ValueError:
            hcl_valid = False
        else:
            hcl_valid = True
    else:
        hcl_valid = False
    
    ecl = document["ecl"]

    pid = document["pid"]
    if len(pid) == 9:
        try:
            int(pid)
        except ValueError:
            pid_valid = False
        else:
            pid_valid = True
    else:
        pid_valid = False

    return (byr >= 1920 and byr <= 2002 and
            iyr >= 2010 and iyr <= 2020 and
            eyr >= 2020 and eyr <= 2030 and
            valid_hgt and
            hcl_valid and
            ecl in "amb blu brn gry grn hzl oth".split() and
            pid_valid)


if __name__ == "__main__":
    main()