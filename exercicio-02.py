
numero_de_moradores = input(str('Numero de Moradores: '))
lista = []
mais_utilizado = 0

for i in range(int(numero_de_moradores)):
    while (True):
        freq = input(
            str('Qual elevador utiliza com mais frequencia, A, B ou C? ')).upper()
        if (len(freq) == 0):
            print('Responda a pergunta por favor!')
        if (freq != 'A') and (freq != 'B') and (freq != 'C'):
            print('Opcao invalida!')
        else:
            break

    while (True):
        periodo = input(str(
            'Em que periodo voce utiliza esse elevador? (M - Matutino, V - Vespertino, N - Noturno) ')).upper()
        if (len(periodo) == 0):
            print('Responda a pergunta por favor!')
        if (periodo != 'M') and (periodo != 'V') and (periodo != 'N'):
            print('Opcao invalida!')
        else:
            break

    lista.append([freq, periodo])

print(lista)


def funcao(elevador, item):
    if (item[0] == elevador):
        return True
    return False


a = list(filter(lambda x: x[0] == 'A', lista))
b = list(filter(lambda x: x[0] == 'B', lista))
c = list(filter(lambda x: x[0] == 'C', lista))

def mais_utilizado():
    if(len(a) == len(b)):
        if(len(b) == len(c)):
            return 'Os três elevadores são utilizados com a mesma frequência.'
        
