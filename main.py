from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
print(len(alphabet))

print(logo)
direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# when user inputs count greater than 25
if shift > 25:
    shift = shift % 25


# combine decrpyt and and encode functions
def caesar(dir, plain_text, shift_amount):
    end_text = ""
    if dir == 'decode':
        shift_amount *= -1
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > len(alphabet) - 1:
            new_position = new_position - len(alphabet)
        new_letter = alphabet[new_position]
        end_text += new_letter
    print(f"The {dir} text is {end_text}")


caesar(dir=direction, plain_text=text, shift_amount=shift)
