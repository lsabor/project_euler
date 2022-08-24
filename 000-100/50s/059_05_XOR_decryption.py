"""
## XOR decryption
Problem 59

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

Link: https://projecteuler.net/problem=59

Date solved:  
2022/07/26
"""

# TODO: refactor for speed

ANSWER = 129448

# imports

from maths.math import product
import string

# solution

file_name = "problem_files/p059_cipher.txt"
with open(file_name, "r") as f:
    message = f.read()
message = message.split(",")
message = list(map(int, message))


def decrypt(message, key):
    key_len = len(key)
    i = 0
    decrypted = []
    for char in message:
        new_val = char ^ key[i]
        decrypted.append(new_val)
        i = (i + 1) % key_len
    return decrypted


def to_ascii(list):
    return "".join(chr(n) for n in list)


def from_ascii(string):
    return [ord(n) for n in string]


def find_reasonable_message(message):

    alphebet = string.ascii_lowercase

    space_count = 0
    for key in product(*[alphebet] * 3):
        key = list(map(ord, key))
        decrypted = decrypt(message, key)

        count = sum(
            (x == 32) for x in decrypted
        )  # count the number of spaces in the decrypted message
        if count > space_count:
            best_message = decrypted
            space_count = count
    return best_message


def solution(bypass=True):
    if bypass:
        return ANSWER

    return sum(find_reasonable_message(message))


if __name__ == "__main__":
    solution(bypass=False)
