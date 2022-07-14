"""
    PROJECT- "CAESAR CIPHER"    
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e',
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text =''
    # print("My type is: ",type(plain_text)) #   gives str

    for letter in plain_text:

        position = alphabet.index(letter) + shift_amount
        if position > len(alphabet):
            new_alpha_index = alphabet.index(letter) + alphabet
        new_letter = alphabet[position] # It is removed for above code.
        cipher_text += new_letter   # It is removed for above code.
    print(f"The encoded text is {cipher_text}.")
    
    #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    plain_text = ''
    for crypt_letter in cipher_text:
    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the 
    # alphabet by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"
        decrypt_position = alphabet.index(crypt_letter) - shift_amount
        decrypt_letter = alphabet[decrypt_position]
        plain_text += decrypt_letter
    print(f"The decoded text is {plain_text}.")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 
# 'direction' variable. Then call the correct function based on that 'direction' variable. 
# You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
    encrypt(plain_text= text, shift_amount= shift)
elif direction == 'decode':
    decrypt(cipher_text= text, shift_amount= shift)
else:
    print("Invalid input.")