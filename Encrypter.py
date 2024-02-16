def encrypt(original_word, modifier, *mod_modifier):
    if not mod_modifier:
        mod_modifier = 0
    else:
        mod_modifier = sum(mod_modifier)
    if modifier < 0:
        negative = -1
    else:
        negative = 1

    # list setup
    #alphabet = [chr(char) for char in range(ord("a"), ord("z") + 1)]
    #digits = [chr(num) for num in range(ord('0'), ord('9') + 1)]
    ascii_characters = [chr(char) for char in range(128)]
    alphabet = ascii_characters
    digits = ascii_characters

    # encrypter
    encrypted_word = ""
    for char in original_word:
        if char.lower() in alphabet:
            index_num = alphabet.index(char.lower())
            while (index_num + modifier) * negative >= len(alphabet):
                index_num -= len(alphabet) * negative
            x_char = alphabet[(index_num + modifier) * negative]
            if char.isupper():
                x_char = x_char.upper()
        elif char in digits:
            index_num = digits.index(char.lower())
            while index_num + modifier >= len(digits):
                index_num -= len(digits)
            x_char = digits[index_num + modifier]
        else:
            x_char = char
        encrypted_word = encrypted_word + x_char
        modifier += mod_modifier

    return encrypted_word


original_word = input("What message do you want to encrypt?\n")

while True:
    modifier = input("How many characters up or down do you want to change it by?\n")
    if modifier.replace("-", "").isdigit():
        modifier = int(modifier)
        break
    else:
        print("\033[F\033[K", end="")
        print("\033[F\033[K", end="")

while True:
    mod_modifier = input("How many numbers do you want to change the modifier by after each encryption?\n")
    if mod_modifier.replace("-", "").isdigit():
        mod_modifier = int(mod_modifier)
        break
    else:
        print("\033[F\033[K", end="")
        print("\033[F\033[K", end="")

print(encrypt(original_word, modifier, mod_modifier))
