def blorakeygen():
    from colorama import Fore, Back, Style
    print("KEY GENERATOR :")
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    print(Fore.GREEN)
    savkey = AESGCM.generate_key(bit_length=256)
    print("We generated a 256-bit key for you!")
    print(Style.RESET_ALL)
    print('The key is "' + str(savkey) + '"')
    print(Fore.GREEN)
    print('Remove the double quotes !')
    print(Style.RESET_ALL)
    print("Make sure to copy it!")


# basic keygen with Python