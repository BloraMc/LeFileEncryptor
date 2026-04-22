import os
import ast
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def bloradecrypt():
    print("FILE DECRYPTER :")
    raw_key = input("What key do you want to use? : ").strip()
    
    try:
        keytouse = ast.literal_eval(raw_key)
    except (ValueError, SyntaxError):
        print("Invalid key format. Include the b and the quotes.")
        return

    if len(keytouse) != 32:
        print(f"Error: Key must be 32 bytes. Yours is {len(keytouse)}.")
        return

    path = input("Enter path of a .lefileencrypter file : ").strip('" ')
    if not os.path.exists(path):
        print("Error: File path does not exist.")
        return

    with open(path, 'rb') as f:
        file_data = f.read()

    nonce, ciphertext = file_data[:12], file_data[12:]
    aesgcm = AESGCM(keytouse)
    
    try:
        decrypted_data = aesgcm.decrypt(nonce, ciphertext, None)
    except:
        print("Aww ... Failed! Wrong key or corrupted file...")
        return

    final_out = path.rsplit(".lefileencrypter", 1)[0] if path.lower().endswith(".lefileencrypter") else path + ".decrypted"

    with open(final_out, 'wb') as f:
        f.write(decrypted_data)

    print(f"Done :D decrypted to: {final_out}")