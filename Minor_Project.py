# MORSE CODE
MORSE_DICT = {'0': '-', '1': '.', '2': '--', '3': '-.', '4': '.-',
              '5': '..', '6': '---', '7': '--.', '8': '-.-', '9': '-..',
              'A': '.--', 'B': '.-.', 'C': '..-', 'D': '...', 'E': '----', 'F': '---.',
              'G': '--.-', 'H': '--..', 'I': '-.--', 'J': '-.-.', 'K': '-..-', 'L': '-...',
              'M': '.---', 'N': '.--.', 'O': '.-.-', 'P': '.-..', 'Q': '..--', 'R': '..-.',
              'S': '...-', 'T': '....', 'U': '-----', 'V': '----.', 'W': '---.-', 'X': '---..',
              'Y': '--.--', 'Z': '--.-.',
              ',': '--..-', '.': '--...', '?': '-.---', '/': '-.--.', '-': '-.-.-',
              '_': '-.-..', '(': '-..--', ')': '-..-.', '+': '-...-', '*': '-....',
              '%': '.----', '&': '.---.', '#': '.--.-', '@': '.--..'}


def encode(msg):
    emsg = ''
    for letter in msg:
        if letter != ' ':
            emsg += MORSE_DICT[letter] + ' '
        else:
            emsg += ' '
    return emsg


def decode(msg):
    msg += ' '
    dmsg = ''
    a = ''
    for letter in msg:
        if ( letter != ' '):
            i = 0
            a += letter
        else:
            i += 1
            if i == 2 :
                dmsg += ' '
            else:
                dmsg += list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(a)]
                a = ''
    return dmsg


def main():
    msg = input()
    result = encode(msg.upper())
    print (result)
    msg = input("enter input in (.) & (-)")
    result = decode(msg)
    print (result)
if __name__ == '__main__':
    main()
