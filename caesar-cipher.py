### Question 1 ################################################################################
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

pairs = {}
ciphertext = ""
plainText = input("Plain Text: ")
shift = int(input("Shift: "))

for letter in alphabet:
    # no literals just in case the alphabet changes :)
    # supports user generated alphabets??
    char = (ord(letter) + shift) - ord(alphabet[0]) # Shift and normalize
    char = (char % len(alphabet)) + ord(alphabet[0]) # mod and de-normalize
    pairs[letter] = chr(char)

for letter in plainText.lower():
    if letter in alphabet:
        ciphertext += pairs[letter]
    else:
        ciphertext += letter

print(ciphertext)

### Question 2 ################################################################################
