alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = 0
while n == 0:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    
    def encode():
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encoded_word = ""

        for letter in text:
            if letter in alphabet:
                n_letter = alphabet.index(letter) + shift
                while n_letter>=26:
                    n_letter = n_letter-26
                print("this",n_letter)    
                encoded_word += alphabet[n_letter]
                
            else:
                encoded_word +=letter
            print (encoded_word)            
        return encoded_word,shift
    def decode(text,shift):
        decoded_word =""
        for letter in text:
            if letter in alphabet:
                
                n_letter = alphabet.index(letter) - shift
                while n_letter < 0:
                    n_letter = n_letter+26
                print("this",n_letter) 
                decoded_word += alphabet[n_letter]
            else:
                decoded_word +=letter  
            print (decoded_word)            

        return decoded_word     

    if direction == "encode" or direction == "e":
        encoded_word,shift = encode()
        
        print(encoded_word)

    if direction =="decode" or direction == "d":
        
        try:
            encoded_word
        except NameError:
            print("No encoding done")
            break

            
        decoded_word = decode(encoded_word,shift)
        print(decoded_word)        

    answer = input("Do you want to try it again? Y/N?  ").lower()
    
    if answer == "n":
        n = 1
    elif answer == "y":
        n=0
    else:
        print("Wrong input")   
        break     
        


print("Thank you! Have a great day")    