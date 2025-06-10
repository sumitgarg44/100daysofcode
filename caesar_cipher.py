from static.arts import caesarcipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(caesarcipher.logo)

def cesar(user_text, shift_amount, user_direction):
    cesar_text = ""
    for char in user_text:
        if char in alphabet:
            position = alphabet.index(char)

            if user_direction == "encode":
                shift_position = position + shift_amount
                if shift_position > 25:
                    shift_position = (shift_position - 25) - 1
            elif user_direction == "decode":
                shift_position = position - shift_amount

            cesar_text += alphabet[shift_position]
        else:
            cesar_text += char

    print(f"\nThe {user_direction} text is: {cesar_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    if direction != "encode" and direction != "decode":
        print("\nOops! You selected incorrect cipher direction.")
    else:
        cesar(user_text=text, shift_amount=shift, user_direction=direction)

    result = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n")

    if result == "no":
        should_continue = False
