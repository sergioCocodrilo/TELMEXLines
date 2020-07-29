



def read_file(in_file):
    module = slice(9, 16)
    pair   = slice(28, 32)
    num    = slice(33, 44)
    _type  = slice(51, 62)
    state  = slice(63, 69)
    modules = {}
    total_modules = 0
    asigned_lines = 0
    with open(in_file, 'r') as f:
        for l in f:
            if l[module].startswith("H'"):
                total_modules += 1
                if l[num].strip() != '':
                    asigned_lines += 1
    print('total_modules:', total_modules)
    print('asigned_lines:', asigned_lines)

                
    

if __name__ == "__main__":
    read_file('157_24junio2020')
