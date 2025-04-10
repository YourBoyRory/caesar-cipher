from random import randint

### Question 1 ################################################################################
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

pairs = {}
ciphertext = ""
plainText = "" #input("Plain Text: ")
shift = 0 #int(input("Shift: "))

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

def roll(d_type):
    output = 0
    amount, die = d_type.split("d")
    for i in range(int(amount)):
        if die == '100':
            output += ((randint(1,int(die)) + 9) // 10) * 10
        elif die == '10':
            output += randint(0,int(die)-1)
        else:
            output += randint(1,int(die))
    return output

count = 10
for i in range(3):
    print(count)
    print("    4: ", roll(f'{count}d4')/count)
    print("    6: ", roll(f'{count}d6')/count)
    print("    8: ", roll(f'{count}d8')/count)
    print("    10: ", roll(f'{count}d10')/count)
    print("    12: ", roll(f'{count}d12')/count)
    print("    20: ", roll(f'{count}d20')/count)
    print("    100: ", roll(f'{count}d100')/count)
    count *= 10
