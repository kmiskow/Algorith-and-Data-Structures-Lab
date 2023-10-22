import sys


class BadCleanup(Exception):
    pass


def decode_line(line_str : str):
    morse_code = {
        'a' : '.-',   'b' : '-...', 'c' : '-.-.',
        'd' : '-..',  'e' : '.',    'f' : '..-.',
        'g' : '--.',  'h' : '....', 'i' : '..',
        'j' : '.---', 'k' : '-.-',  'l' : ".-..",
        'm' : '--',   'n' : '-.',   'o' : '---',
        'p' : '.--.', 'q' : '--.-', 'r' : '.-.',
        's' : '...',  't' : '-',    'u' : '..-',
        'v' : '...-', 'w' : '.--',  'x' : '-..-',
        'y' : '-.--', 'z' : '--..', ' ' : '/'
    }

    morse_code_string = ''

    for char in line_str:
        if char not in morse_code:
            raise BadCleanup
        morse_code_string += f"{morse_code[char]} "
    
    return morse_code_string


def cleanup(line_str : str):
    clean_line = ""
    space = True
    for char in line_str:
        if not str.isalpha(char) and char != ' ':
            continue
        if char == ' ':
            if space:
                continue
            clean_line += char
            space = True
            continue
        clean_line += str.lower(char)
        space = False
    if clean_line[-1] == ' ':
        clean_line = clean_line[:-1]
    return clean_line
        

def get_file(file_name : str):
    with open(file_name, 'r') as file_handle:
        lines = file_handle.readlines()
    return lines
        

def main(argv):
    lines = get_file(argv[1])
    for line in lines:
        print(decode_line(cleanup(line)))


if __name__ == "__main__":
    main(sys.argv)