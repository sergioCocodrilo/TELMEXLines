

import pandas as pd

def read_file(in_file):
    # input structure
    module = slice(9, 16)
    pair   = slice(28, 32)
    num    = slice(33, 44)
    _type  = slice(51, 62)
    state  = slice(63, 69)
    modules = {}

    # output CSV file
    df = pd.DataFrame(columns = ['module', 'pair', 'num', 'type', 'state'])
    index = 0
    i = 0
    with open('data/input/' + in_file, 'r') as f:
        for l in f:
            print(i*100//41150 , '%', end='\r')
            i += 1
            if l[module].startswith("H'"):
                df.loc[index] = [l[module].strip(), l[pair].strip(), l[num].strip(), l[_type].strip(), l[state].strip()]
                index += 1

    df.to_csv('data/output/' + in_file.split('.')[0] + '.csv', index=False)
    print('Archivo guardado como:', in_file.split('.')[0] + '.csv')



if __name__ == "__main__":
    while True:
        file_name = input('Nombre del archivo a analizar: ')
        try:
            f = open('data/input/' + file_name, 'r')
        except FileNotFoundError:
            print('Archivo no encontrado. Verifica el nombre.')
        else:
            f.close()
            break
    
    read_file(file_name)
