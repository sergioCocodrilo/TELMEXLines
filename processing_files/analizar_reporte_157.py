
"""
Reads a S12 report from instruction 157
and produces a CSV file from its data.
"""


def read_file(in_file):
    module = slice(9, 16)
    pair   = slice(28, 32)
    num    = slice(33, 44)
    _type  = slice(51, 62)
    state  = slice(63, 69)
    modules = {}
    f_out = open("modulos_avpark", 'w')
    with open(in_file, 'r') as f:
        for l in f:
            if l[module].startswith("H'") and l[state] == "AVPARK":
                f_out.write(l[module] + "\t" + l[pair] + "\t" + l[num] + "\t" + l[_type] + "\t" + l[state] + "\n")
                modules[l[module]] = modules.get(l[module], 0) + 1
    f_out.close()
                
    f_out = open("modulos_mas_afectados", 'w')
    f_out.write("MODULO\tINCIDENCIAS")
    [f_out.write(k + "\t" + str(v) + "\n") for k, v in sorted(modules.items(), key=lambda x: x[1])]
    f_out.close()
    

if __name__ == "__main__":
    read_file('157_24junio2020')
