"""
    PROJECT- "CAESAR CIPHER"    
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e',
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# cipher_letter = []

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 
# 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    cipher_text =''
    print("My type is: ",type(plain_text)) #   gives str

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' 
    # forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    for letter in plain_text:
        # --> Finding position of letter in alphabet list
        # print(alphabet.index(letter))
        position = alphabet.index(letter) + shift_amount
        if position > len(alphabet):
            new_alpha_index = alphabet.index(letter) + alphabet
        """
        cipher_letter.append(alphabet[position]) # OR 
        # print(cipher_letter)
        cipher_text = ''.join(cipher_letter)
    """
        new_letter = alphabet[position] # It is removed for above code.
        cipher_text += new_letter   # It is removed for above code.
    print(f"The encoded text is {cipher_text}.")

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should .
# be able to test the code and encrypt a message. 
encrypt(plain_text= text, shift_amount= shift)