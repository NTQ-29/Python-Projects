CC_LETTERS = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(CC_LETTERS)

#def encrypt(plaintext, key):
   # text_cipher = ''
   # for letter in plaintext:
    #    letter = letter.lower()
      #  if not letter == ' ':
        #    index = CC_LETTERS.find(CC_LETTERS)
         #   if index == -1:
          #      text_cipher += letter
          #  else:
            #    new_index = index + key
            #    if new_index >= num_letters:
             #       new_index -= num_letters
            #    text_cipher += CC_LETTERS[new_index]
  #  return text_cipher

#def decrypt(text_cipher, key):
 #   plaintext = ''
  #  for letter in text_cipher:
#        letter = letter.lower()
   #     if not letter == ' ':
  #          index = CC_LETTERS.find(CC_LETTERS)
   #         if index == -1:
    #            plaintext += letter
    #        else:
     #           new_index = index + key
     #           if new_index < 0:
      #            new_index += num_letters
      #          plaintext += CC_LETTERS[new_index]
   # return plaintext

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key

    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = CC_LETTERS.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += CC_LETTERS[new_index]
    return result


print()
print("**CAESAR CIPHER**")
print()

print("Do you plan to encrypt or decrypt?")
user = input('e/d: ').lower()

print()
if user == 'e':
    print("ENCRYPTION MODE ACTIVATED")
    print()
    key = int(input("Enter key here (1 through 26): "))
    text = input("Enter text to encrypt: ")
    text_cipher = encrypt_decrypt(text, user,  key)
    print(f'CIPHERTEXT: {text_cipher}')

elif user == 'd':
    print("DECRYPTION MODE ACTIVATED")
    print()
    key = int(input("Enter key here (1 through 26): "))
    text = input("Enter text to dencrypt: ")
    plaintext = encrypt_decrypt(text, user, key)
    print(f'PLAINTEXT: {plaintext}')
