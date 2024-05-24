print(' ')
print('Would you like to encode or decode a string?')
DecodeOrEncode = input ()
print(' ')

if DecodeOrEncode != 'decode' and DecodeOrEncode != 'encode': 
    print('Please write decode or encode')
    exit()

if DecodeOrEncode == 'encode':
    print('What encode key would you like to use? Please provide an integer. Provide one integer if you want a Caesar Cipher.')
    print('Provide mulitple integers seperated by a space for a vigenère cypher: ')
    EncodeKey = str(input())
    modifier = 1

if DecodeOrEncode == 'decode':
    print('What encoding key was used to encode this string? Please provide an integer: ')
    print('If it is a vigenère cypher provide the same key in the same order used to encrypt it, all integers seperated by spaces')
    EncodeKey = str(input())
    modifier = -1

# Checking if the key consists only of integers and spaces.

validkeycharacters = '1234567890 '
encryptpos = 0
firsterror = False
 
for encrypter in EncodeKey:
    if encrypter not in validkeycharacters and firsterror == True:
        print(encrypter)
    if encrypter not in validkeycharacters and firsterror == False:
        print('Your key contains characters that are not integers. Namely: ')
        print(encrypter)
        firsterror = True
    encryptpos = encryptpos + 1
    if encryptpos == len(EncodeKey) and firsterror == True:
        exit()

# This changes the key provided by the user into a list

encodelist = []
space = ' '
alphabet_s = 'abcdefghijklmnopqrstuvwxyz'
alphabet_l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

EncodeKey = str(EncodeKey)
for integer in EncodeKey:
    if integer not in space:
        integer = int(integer) % len(alphabet_s)
        encodelist.append(integer)

print('Please provide the string you wish to ' + DecodeOrEncode)
userinput = str(input())

# This changes the user input string into a list

thelist = []
for character in userinput:
    thelist.append(character)

# The for loop below actually encodes the provided string

currentposition = 0
currentkeyposition = 0

for letter in thelist:
    if letter in alphabet_s:
        index_alphabet_s = alphabet_s.find(thelist[currentposition])
        index_alphabet_s = (index_alphabet_s + modifier * encodelist[currentkeyposition]) % (modifier * len(alphabet_s))
        thelist[currentposition] = alphabet_s[index_alphabet_s]
    if letter in alphabet_l:
        index_alphabet_l = alphabet_l.find(thelist[currentposition])
        index_alphabet_l = (index_alphabet_l + modifier * encodelist[currentkeyposition]) % (modifier * len(alphabet_l))
        thelist[currentposition] = alphabet_l[index_alphabet_l]
    currentposition = currentposition + 1
    currentkeyposition = currentposition % len(encodelist)


# This changes the encoded list back into a string
userinput = ''
for element in thelist:
    userinput = userinput + str(element)

print(' ')
print(userinput)
print(' ')