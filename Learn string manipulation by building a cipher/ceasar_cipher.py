text = 'freeCodeCamp'
shift = 3

# initiate function
def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    # Loop the string text and convert them into lowercase
    for char in message.lower():
        # make condition if the current character is space
        if char == ' ':
            encrypted_text += char
        else:
            # find in the alphabet the current char and store to index
            index = alphabet.find(char)

            # current index plus shift, and use modulo operator to get the remainder of the length of alphabet
            new_index = (index + offset) % len(alphabet)

            # store in the encrypted text the current encrypted alphabet
            encrypted_text += alphabet[new_index]

    print('Plain text:', message)
    # Outside loop, print the complete encryption of text
    print('Encrypted text:', encrypted_text)

# Call the function
caesar(text, shift)