# LeFileEncryptor main file
# Needs to be basic to work anywhere but still advenced
# DO NOT use Windows or Linux specific commands (mass compatibility required)

from colorama import Fore, Back, Style
import os
import time
import cryptography
import blorakeygen
import bloraencrypt
import bloradecrypt

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

data = "None"

clear()
print(Fore.GREEN + "----- LeFileEncryptor -----")
print(Style.RESET_ALL)
print("Made by BloraMc with ❤️  and Python")
print("LeFileEncryptor is licensed under MIT license")
print("This software has been made in 2026 and may not")
print("meet the security requirements in the future !")
print(Style.DIM)
print("https://lystech.org/")
print(Style.RESET_ALL)
input("Open the main menu? [ENTER]")

while True:
    clear()
    print(Fore.GREEN)
    choice = input("What would you like to do?\n encrypt [E] decrypt [D] generate key [K] exit [X]\n")
    print(Style.RESET_ALL)
    match choice:
        case "e":
            bloraencrypt.bloraencrypt()
            input("\nGo back to main menu?")
        case "d":
            bloradecrypt.bloradecrypt()
            input("\nGo back to main menu?")
        case "k":
            blorakeygen.blorakeygen()
            input("\nGo back to main menu?")
        case "x":
            print(Fore.BLUE)
            print("Exiting ...")
            time.sleep(1)
            print(Style.RESET_ALL)
            exit()
        case _:
            print(Fore.RED)
            print("Invalid Choice!")
            print(Style.RESET_ALL)
            input("\nGo back to main menu?")