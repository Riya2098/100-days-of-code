
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    revised_message=[]
    for i in range(len(text)):
        x=alphabet.index(text[i])
        x=x+shift
        if(x>=26):
            x= x-26
        revised_message.append(alphabet[x])
    text="".join(revised_message)
    print(f"The Encoded text is: {text}")

def decrypt(text, shift):
    finalText=""
    for j in text:
        y=alphabet.index(j)
        new_indice= y-shift
        if(new_indice<0):
            new_indice=26 +new_indice
        finalText+=alphabet[new_indice]
    print(f"The Decoded text is: {finalText}")

def caesar(direction, text, shift):
    finalAnswer=""
    if(direction=='decode'):
        shift*= -1
    for j in text:
        if j in alphabet:
            position= alphabet.index(j)
            # print(f"Letter is: {j}")
            # print(f"Initial position is: {position}")
            new_position = position + shift
            # print(f"New position is: {new_position}")
            finalAnswer+=alphabet[new_position]
        else:
            finalAnswer+=j
        
    print(f"The {direction}d message is: {finalAnswer}")

print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

should_continue=True

while(should_continue):

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if(shift>26):
        shift=shift%26
        caesar(direction, text, shift)
    else:
        caesar(direction, text, shift)
    
    result= input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if(result=='no'):
        should_continue=False
        print("Goodbye!")
    