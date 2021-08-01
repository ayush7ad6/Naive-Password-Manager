from crypto import get_path
import getpass

dirpath = get_path()

print("")
masterkey = getpass.getpass(
    "Enter the new master key for your Naive Password Manager: ")

prime = 91
hash1 = 0
for i in masterkey:
    hash1 = ord(i) + prime*hash1

with open(dirpath+'//masterkey.txt', 'w') as file:
    file.write(str(hash1))
