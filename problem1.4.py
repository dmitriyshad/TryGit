import string

def read_length(filename):
    return int(filename.readline())

def parse_text(filename):
    with open(filename, 'r') as f:
        strlen = read_length(f)
        for line in f:
            print_parts_of_line(line, strlen)

def print_parts_of_line(line, strlen):
    words = line.split(' ')
    curlen = strlen + 1
    curstr = []
    for word in words:
        if word[len(word) - 1] == '\n':
            word = word[:-1]
        if len(word) + 1 <= curlen:
            curstr.append(word)
            curlen -= (len(word) + 1)
        elif curlen == strlen + 1:
            print word
        else:
            print ' '.join(curstr)
            curstr = [word]
            curlen = strlen - len(word)
    print ' '.join(curstr)

parse_text('input.txt')
