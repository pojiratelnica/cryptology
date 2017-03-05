alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getText():
    text = open('plaintext.txt').read()
    return(text)


def setText(encrypted):
    text = open('ecryptedtext.txt', 'w')
    print(encrypted, file=text)
    text.close()
    return('Encrypted')


def encrypt(key, plaintext):
    cyphertext = ''
    plaintext = plaintext.upper()
    for i in plaintext:
        if i.isalpha():
            indexof = alphabet.index(i)
            enc = (indexof + key) % len(alphabet)
            cyphertext += alphabet[enc]
        else:
            cyphertext += i
    return(cyphertext)


def ceasar():
    s = getText()
    c = encrypt(3, s)
    setText(c)

if __name__ == '__main__':
    ceasar()
