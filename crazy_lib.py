def make_crazy_lib(filename):
    file=open(filename,'r')
    text=''
    for line in file:
        text = text+process_line(line)
    file.close()
    return text

def process_line(line):
    placeholders=['NOUN','ADJECTIVE','VERB_ING','VERB']
    process_line = ''
    words = line.split()
    for word in words:
        if word in placeholders:
            answer = input('enter a ' + word + ': ')
            process_line = process_line + answer + ' '
        else:
            process_line = process_line +word + ' '

    return process_line + '\n'



def main():
    lib = make_crazy_lib('lib.txt')
    print(lib)

if __name__ == '__main__':
    main()