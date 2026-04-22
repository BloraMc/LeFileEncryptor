# LeFileEncryptor

"LeFileEncryptor" is a CLI + web based app to encrypt any files/data to AES-256 with a key generator

Made by me with ❤️ and Python

LeFileEncryptor uses AES encryption (256 bits) to encrypt or decrypt any provided data.
LeFileEncryptor is a CLI app licensed under MIT and can be used on Windows, Linux & MacOS

Since LeFileEncryptor is based on Python, you can use it by running it from the source code, simply by cloning the repo & downloading the required packages with the following command :

`pip install -r requirements.txt`

LeFileEncryptor has been made on Python 3.11, it may not work on other versions such as 3.9, or 3.14 !
This data encrypting software LeFileEncryptor saves files in `.lefileencrypter` and needs to be decrypted with LeFileEncrypter
Exemple : If you encrypt image.png, the encrypted file will be called image.png.lefileencrypter, and when decrypted will be back to image.png