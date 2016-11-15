#ciphertext='yrd nslxv stnwfmkbk ayaw? fdetuawg lnk iqxet vmgh! stnwfmkb ztv rg bhigyjskk, qxvlc!'
ciphertext='vad heter fantomens hund? fantomen har ingen hund! fantomen har en bergsvarg, devil!'
key='dragostenta'
alphabet='abcdefghijklmnopqrstuvwxyz'
values=[]
output=[]
mode='kryptering'
#mode='dekryptering'
'''for x in key:
    values.append(ord(x)-97)
counter = 0
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
print(''.join(output))'''
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

print(vigenere(ciphertext,key,alphabet,mode))