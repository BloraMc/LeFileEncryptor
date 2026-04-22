import os
import ast
import random
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def bloraencrypt():
    print("FILE ENCRYPTER :")
    raw_key = input("What key would you like to use? : ")
    try:
        keytouse = ast.literal_eval(raw_key)
    except:
        print("Invalid key format.")
        return

    if len(keytouse) != 32:
        raise ValueError(f"Key must be 32 bytes. Yours is {len(keytouse)} bytes.")

    path = input("Path of file to encrypt : ").strip('"')
    save_in = input("Path of where to save : ").strip('"')

    with open(path, 'rb') as f:
        data = f.read()

    aesgcm = AESGCM(keytouse)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, data, None)

    # Logic to keep the original extension in the name
    orig_name = os.path.basename(path)
    if os.path.isdir(save_in) or save_in.endswith(('/', '\\')):
        final = os.path.join(save_in, orig_name + ".lefileencrypter")
    else:
        # If user provides a custom path/name, we still force the extension
        final = save_in if save_in.endswith(".lefileencrypter") else save_in + ".lefileencrypter"

    with open(final, 'wb') as f:
        f.write(nonce + ct)

    print(f"Encrypted data saved to: {final}")