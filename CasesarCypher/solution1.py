

# unicode approach
# a -> 97, z -> 122

def caesar_cipher(str, key):
    if key < 1:
        print("invalid key")
        return

    # edge case - mod the key to wrap around the alphabet
    key %= 26

    result = ""

    for i in str:
        # get the unicode equivalent of each char
        letter_code = ord(i)
        # convert unicode equivalent to shifted value
        # when the value is <= 'z', convert straight into a character
        if key <= 122:
            new_letter_code = letter_code + key
        # but when the value is > 'z' we need to 'modulo' it, unicode style
        elif key > 122:  # key is not in range
            # start at the letter before 'a' add the remainder of the value
            # mod 122
            new_letter_code = 96 + (new_letter_code%122)

        # convert back to character and add to result
        result += chr(new_letter_code)

    print(str)
    print(result)

if __name__ == "__main__":
    caesar_cipher("abcdefg", 5)
    print()
    caesar_cipher("abcdefg", 122)
    print()
    caesar_cipher("abcdefg", 123)
    print()
    caesar_cipher("abcdefg", 4000)

