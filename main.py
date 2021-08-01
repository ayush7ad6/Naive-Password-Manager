from func import create, menu, masterkey, profile, view
import os
import time
import getpass


os.system('cls')
maskey = getpass.getpass("Enter the master key: ")

if masterkey(maskey):
    os.system('cls')
    temp = '\t-Access Granted-'
    for i in temp:
        print(i, end="")
        # time.sleep(0.15)
    print("")

else:
    time.sleep(0.7)
    print('(⇀‸↼‶)')
    exit()

active_profile = profile()
os.system('cls')


option = menu(active_profile)
while option != 'goodbye' and option != 'bye' and option != 'q' and option != 'exit':
    if option == '1':
        create(active_profile)

    if option == '2':
        view()

    if option == '3':
        active_profile = profile()

    os.system('cls')
    option = menu(active_profile)

exit()
