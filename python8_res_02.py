# python file for exemple [Python_08.fasta](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_08.fasta)

import sys

# opening the file placed at terminal by the user
fasta_filename = sys.argv[1]
fasta_filehandle = open(fasta_filename, 'r') 

seq_id = None
seq_string = ''

for line in fasta_filehandle:
    line = line.rstrip() 

    if line.startswith('>'):
        if len(seq_string) > 0:
            print(seq_id + "-frame" + str(1) + "-codons")
            sep = ''  
            for offset in range(0, len(seq_string), 3):
                print("{0}{1}".format(sep, seq_string[offset:offset+3]), end='')
                sep=' '
            print()  

        seq_def = line.lstrip('>').split(' ', maxsplit=1)
        seq_id = seq_def[0]
        seq_string = ''  # make empty again for new seq
        
    else:
        seq_string += line.upper()

if len(seq_string) > 0:
    print(seq_id + "-frame" + str(1) + "-codons")
    sep = ''  
    for offset in range(0, len(seq_string), 3):
        print("{0}{1}".format(sep, seq_string[offset:offset+3]), end='')
        sep=' '
                
    print()