import hashlib

key_start = "bgvyzdsv"

i = 0
while True:
    key = f"{key_start}{i}".encode('utf-8')
    h = hashlib.md5(key)
    hex_string = h.hexdigest()
    if hex_string[:6] == "0"*6:
        break
    i += 1

print(i)  # answer: 1038736
