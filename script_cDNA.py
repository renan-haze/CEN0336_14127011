import sys

#colocando todos os argumentos em caps lock
dna_sequence = sys.argv[1].upper()
#atribuindo valores para as coordenadas
n1 = sys.argv [2]
n2 = sys.argv [3]
n3 = sys.argv [4]
n4 = sys.argv [5]

#conferindo se todas os dados estão de forma correta
if dna_sequence.isdigit(): 
   print("the sequence is not correct")
elif len(dna_sequence) < int(n1) | int(n2) | int(n3) | int(n4):
    print("the number coordinates are bigger than DNA sequence, please check it again")
else:
    print('the DNA sequence and numbers are good to go!')

#encontrando a posição desejada
dna_sequence.index('ATG')
dna_sequence.index('TGA')

CDS_1 = dna_sequence[19:]
CDS_2 = dna_sequence[:35]

# esse número 19 é a posição onde se encontra a sequencia "ATG"
# embora eu saiba que esse número possa mudar de acordo com o tamanho da sequencia que está sendo analisada, não consegui resolver

# numero 35 é a posição do códon TGA
# a sequencia que deve ser impressa está entre a posição 20 e 36 da sequencia
#concatenação das duas sequencias 
print(CDS_1 + CDS_2)