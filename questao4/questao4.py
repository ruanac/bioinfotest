import itertools as it #importando biblioteca

FILE_INPUT = open("input.txt") # o arquivo precisa está carregado onde será realizado o código
FILE_OUTPUT = open("output.txt", 'w') #O 'w' diz que o arquivo está sendo utilizado para escrita(write) # arquivo de saída
SEQUENCES = []

# Essa função recebe como parâmetro duas strings e o tamanho minimo da sobreposição
# realizando uma sobreposição entre a string_1 e a string_2, garantindo que a string_2
# não seja colocada antes da string_1 para esta sobreposição.
def overlap(string_1, string_2, min_length):
    start = 0
    while True:
        # Procurar na string_1 o prefixo de menor comprimento da string_2 e irá atribuir esse prefixo a variável start
        start = string_1.find(string_2[:min_length], start)
        # Se não houver ocorrência da string_2 na string_1 ele retornará -1, então neste caso ele retornará zero
        if start == -1:
            return 0
        # Mas se existir alguma ocorrência irá retornar o comprimento da sobreposição mais longa entre
        # string_1 e string_2.
        if string_2.startswith(string_1[start:]):
            return len(string_1) - start
        start += 1

# Essa função auxiliar receberá um conjunto de "leituras" e uma sobreposição mínima e retornará as duas leituras com
# a sobreposição máxima junto com a sobreposição.
def pick_maximal_overlap(reads, k):
    read_a = None
    read_b = None
    best_overlap = 0
    # Para cada par de leituras a e b irá calcular o comprimento da sobreposição utilizando o método overlap
    # criado anteriormente
    for a, b in it.permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        # Se o comprimento da sobreposição for maior que o melhor comprimento de sobreposição anterior, salve essa
        # sobreposição como sendo a melhor e retorne essa sobreposição.
        if olen > best_overlap:
            read_a = a
            read_b = b
            best_overlap = olen
    return read_a, read_b, best_overlap

# Essa é a função para descobrir a superstring mais curta que receberá um conjunto para leitura (reads) e um valor
# mínimo para sobreposição (k)
def shortest_common_string(reads, k=1):
    # Para iniciar é necessário calcular apenas as duas leituras (read_a e read_b) com a melhor sobreposição sendo possível
    # encontrar utilizando a função de pick_maximal_overlap criada anteriormente
    read_a, read_b, olen = pick_maximal_overlap(reads, k)
    # Então é necessário um loop executando até que o comprimento da sobreposição seja 0. Então os read_a e
    # read_b são substituidos com a sua sobreposição removendo o read_a e o read_b do conjunto de reads e depois anexando a essa lista
    # (reads) a combinação dos read_a e read_b. E isso será feito vez após vez até só obter uma leitura restante, que
    # será nossa superstring mais curta.
    while olen > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        # Agora é preciso recalcular o novo a, b e o comprimento da sobreposição com a maior sobreposição.
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    # Quando isso for feito e as leituras restantes será toda a leitura que não tem nenhuma sobreposição, então é preciso
    # apenas junta-las e essa será nossa superstring.
    return ''.join(reads)

# Essa função pega o conteúdo do arquivo e adiciona na variável sequences e retorna essa sequence para ser utilizada.
def get_text_in_file(file):
    sequence = []
    for line in file:
        sequence.append(line[:-1].strip())
    file.close()
    return sequence

# Essa função recebe como parâmetro o arquivo e o texto e salva o texto dentro do arquivo.
def save_sequence(file, text):
    file.writelines(text)
    file.close()

def main():
    SEQUENCES = get_text_in_file(FILE_INPUT)
    print('Buscando pela menor superstring contendo todas as string, o seu resultado é: ')
    ss = shortest_common_string(SEQUENCES)
    print((ss))
    save_sequence(FILE_OUTPUT, ss)

if __name__ == '__main__':
    main()