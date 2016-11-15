ciphertext=0x2e000d1f0e190d011d4813c295181554011c0f1a410a4b0318070b0b1c4f
key='hackathon'
values=[]
output=[]
alphabet='abcdefghijklmnopqrstuvwxyz'
mode='kryptering'
#mode='dekryptering
def XOR:
    for x in key:
        values.append(ord(x) - 97)
    counter = 0
    if mode == 'dekryptering':

'''
#ciphertext='yrd nslxv stnwfmkbk ayaw? fdetuawg lnk iqxet vmgh! stnwfmkb ztv rg bhigyjskk, qxvlc!'
ciphertext='vad heter fantomens hund? fantomen har ingen hund! fantomen har en bergsvarg, devil!'
key='dragostenta'

'
def vigenere(ciphertext,key,alphabet,mode):
    for x in key:
        values.append(ord(x) - 97)
    counter = 0
    if mode=='dekryptering':
        for x in ciphertext:
            if x in alphabet:
                if ord(x) - values[counter]>96:
                    output.append(chr(ord(x)-values[counter]))
                    counter += 1
                    if counter==len(key):
                        counter=0

                else:
                    output.append(chr(ord(x)-values[counter]+26))
                    counter += 1
                    if counter==len(key):
                        counter=0
            else:
                output.append(x)
    elif mode=='kryptering':
        for x in ciphertext:
            if x in alphabet:
                if ord(x) + values[counter] < 123:
                    output.append(chr(ord(x) + values[counter]))
                    counter += 1
                    if counter == len(key):
                        counter = 0

                else:
                    output.append(chr(ord(x) + values[counter] - 26))
                    counter += 1
                    if counter == len(key):
                        counter = 0
            else:
                output.append(x)
    return ''.join(output)

print(vigenere(ciphertext,key,alphabet,mode))'''