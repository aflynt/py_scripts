import sys


def space_word(word, fieldsize):
    '''
    input a word
    return a string filled to fieldsize
    '''
    return f'{word:{fieldsize}s}'

def space_ith_word(words, i=0, fieldwidth=7):

    for j,w in enumerate(words):
        sw = w

        if j == i:
            sw = space_word(w,fieldwidth)

        print(sw,end=' ')
    print()


def process_stdin():
    # space out the first word
    for line in sys.stdin:

        line = line.strip('\n')

        words = line.split(' ')
        space_ith_word(words)
        
process_stdin()
