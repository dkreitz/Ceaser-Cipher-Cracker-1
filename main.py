def caesar_cipher_brute_force_attack(ciphertext):
    with open("output.txt", "w") as output_file:
        for shift in range(26):
            plaintext = ""
            for char in ciphertext:
                if char.isalpha():
                    new_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
                    if char.isupper():
                        new_char = new_char.upper()
                    plaintext += new_char
                else:
                    plaintext += char
            output_file.write(f"Shift: {shift}, Plaintext: {plaintext}\n")

# Read ciphertext from input file
with open("input.txt", "r") as input_file:
    ciphertext = input_file.read().strip()

# Perform brute force attack and write results to output file
caesar_cipher_brute_force_attack(ciphertext)