from cryptography import fernet
from crypto import get_path

key = fernet.Fernet.generate_key()
dirpath = get_path()

print(
    "Warning: The existing key(if any) will be overwritten with the new key. All previous encrypted password will be impossible to retrieve if you proceed to create a new key[y/n]")

input = input()

if input == 'y':
    with open(dirpath+"\\crack.txt", "wb") as keyfile:
        keyfile.write(key)

else:
    exit()
