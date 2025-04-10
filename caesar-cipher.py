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

class Dice:
    def roll(self, d_type, r_count=1):
        amount, die = d_type.split("d")
        amount = amount or '1'
        output = int(die) if r_count < 0 else 0
        for i in range(abs(r_count)):
            total = 0
            for i in range(int(amount)):
                total += randint(1,int(die))
                output = min(output, total) if r_count < 0 else max(output, total)
        return output
        
dice = Dice()
count = 10
for i in range(3):
    print(count)
    print("    4: ", dice.roll(f'{count}d4')/count)
    print("    6: ", dice.roll(f'{count}d6')/count)
    print("    8: ", dice.roll(f'{count}d8')/count)
    print("    10: ", dice.roll(f'{count}d10')/count)
    print("    12: ", dice.roll(f'{count}d12')/count)
    print("    20: ", dice.roll(f'{count}d20')/count)
    print("    100: ", dice.roll(f'{count}d100')/count)
    count *= 10
