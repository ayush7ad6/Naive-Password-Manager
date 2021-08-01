#from func import get_path
import os
from cryptography import fernet
import time
import pyperclip

prime = 91


def check_key(key):
    with open('masterkey.txt') as file:
        secretcode = file.read()
    hash1 = 0
    for i in key:
        hash1 = ord(i) + prime*hash1
    if int(secretcode) == hash1:
        return True
    else:
        return False


def load_crack():
    dir_path = get_path()
    with open(dir_path+'\\crack.txt', 'rb') as crackfile:
        key = crackfile.read()
        return key


def get_path():
    return os.path.dirname(os.path.realpath(__file__))


def encrypt_pass(appname, username, password):
    key = load_crack()
    f = fernet.Fernet(key)

    encryption = f.encrypt(password.encode())

    with open('key.txt', 'a') as keyfile:
        keyfile.write(encryption.decode())
        keyfile.write('\n')

    time.sleep(0.2)
    print('')
    time.sleep(1)
    print('-'*50)
    print('Entry "{}" -> "{}" is saved'.format(appname, username))
    print('-'*50)
    time.sleep(3)


def find_password(appname, line_count):
    key = load_crack()
    f = fernet.Fernet(key)

    with open('key.txt', 'r') as file:
        l = 1
        for line in file:
            if l == line_count:
                encryption = line
                break
            l += 1
        decryption = f.decrypt(encryption.encode())
        thepassword = decryption.decode()
        pyperclip.copy(thepassword)
        time.sleep(0.3)
        print('Password copied to clipboard for 10 seconds!')
        time.sleep(10)
        pyperclip.copy("")
