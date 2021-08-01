# what to import?
from crypto import check_key, encrypt_pass, find_password, get_path
import time
import os


def masterkey(maskey):
    return check_key(maskey)


# def get_path():
#     return os.path.dirname(os.path.realpath(__file__))


def menu(active_profile):
    print('-'*38)
    print('\tNaive Password Manager')  # 22 length
    print('-'*38)
    print('\t\t\t\t\t\t------{}------'.format(active_profile))
    print('1. Create an entry')
    print('2. Retrieve a password')
    print('3. Change profile')
    print("")
    return input('>> ')


def profile():  # cd to the active profile and create username.txt and key.txt and return the active profile name
    dir_path = get_path()
    os.chdir(dir_path)

    f = 0
    valid = ""

    while f == 0:
        print('Provide {} profile to access: '.format(valid), end='')
        alias = input()
        if os.path.isdir(alias) == True:
            f = 1
            os.chdir(alias)
        else:
            print(
                "Profile not found. Want to create profile of {}?[y/n]".format(alias))
            if input() == 'y':

                os.mkdir(alias)
                os.chdir(alias)
                with open('username.txt', 'w'):
                    pass

                with open('key.txt', 'w'):
                    pass

                f = 1
            else:
                valid = 'valid'

    os.system('cls')

    # returnt the profile name
    return alias


def create(profile):
    print("\nProvide the name of the app/website")
    appname = input()

    with open(get_path()+'//'+profile+'//username.txt') as file:
        for line in file:
            words = line.split('\t\t')
            if(words[0] == appname):
                print("\n'{}' already exists".format(appname))
                time.sleep(2)
                return

    print("\nProvide the username")
    username = input()
    if username == None:
        username = ""

    print("\nEnter a strong password for {}{}".format(appname, '->'+username))
    passwd = input()

    encrypt_pass(appname, username, passwd)

    with open('username.txt', 'a') as userfile:
        userfile.write(appname+'\t\t')
        userfile.write(username+'\n')


def view():
    print("\nProvide the app/website to retrieve the password")
    appname = input()

    with open('username.txt') as file:
        l = 1
        f = 0
        for line in file:  # finding username associated with the app/web
            words = line.split('\t\t')
            if words[0] == appname:
                f = 1
                username = words[1]
                print("\nUsername: {}".format(username))
                break
            l += 1
    if f:
        find_password(appname, l)
    else:
        print('\nNo entry as "{}"'.format(appname))
        time.sleep(2)
