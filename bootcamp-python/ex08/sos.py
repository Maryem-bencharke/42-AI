import sys
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
def switch(word):
    c=' '
    for letter in word:
        if letter !=' ':
            c+= MORSE_CODE_DICT + ' '
        else:
            c+=' '
    return c
def switch2(word):
    word +=' '
    d= ''
    b=''
    for letter in word:
        if letter !='':
            i=0
            b += letter
        else:
            i +=1
            if i==2:
                d +=' '
            else:
                d += list(MORSE_CODE_DICT.keys()) [list(MORSE_CODE_DICT.values()).index(b)]
                b=''
    return d
if __name__=='__main':
    if len(sys.argv)>2 or len(sys.argv)<2:
        print('ERROR')
    if len(sys.argv)==2:
        print(switch2(sys.argv[1]))
        