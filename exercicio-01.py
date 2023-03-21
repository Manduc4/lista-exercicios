
# variaveis globais
salario_base = 1320.00

# cargos
gerente = 'G'
operario = 'O'

# turnos
matutino = 'M'
vespertino = 'V'
noturno = 'N'

# erros
errors = []
nome_vazio = 'O Nome e Obrigatorio.'
turno_vazio = 'O Turno e Obrigatorio.'
cargo_vazio = 'O Cargo e Obrigatorio.'

turno_incorreto = 'Insira o turno de acordo com a legenda (M-Matutino, V-Vespertino ou N-Noturno): '
cargo_incorreto = 'Insira o cargo de acordo com a legenda (G-Gerente ou O-Operario): '

def inputNome():
    while (True):
        nome = input('Nome: ').upper()
        if (len(nome) == 0):
            print(nome_vazio)
        else:
          break
    return nome

def inputTurno():
    while (True):
        turno = input('Turno: ').upper()
        if (len(turno) == 0):
            print(turno_vazio)
        elif (turno != 'M') and (turno != 'V') and (turno != 'N'):
            print(turno_incorreto)
        else:
            break
    return turno

def inputCargo():
    while (True):
        cargo = input('Cargo: ').upper()
        if (len(cargo) == 0):
            print(cargo_vazio)
        elif (cargo != 'G') and (cargo != 'O'):
            print(cargo_incorreto)
        else:
            break
    return cargo

def inputQuantidadeHorasTrabalhadas():
    while (True):
        qtd_horas_trabalhadas = int(input('Quantidade de Horas Trabalhadas: '))
        if (len(str(qtd_horas_trabalhadas)) == 0):
            print('A quantidade de horas é Obrigatória')
        else:
            break
    return qtd_horas_trabalhadas
        
def generalInput():
    nome = inputNome()
    turno = inputTurno()
    cargo = inputCargo()
    qtd_horas_trabalhadas = inputQuantidadeHorasTrabalhadas()
    return [nome, turno, cargo, qtd_horas_trabalhadas]


def getValorPercentual(turno, cargo):
    valor_percentual = 0
    if cargo == gerente:
        # Categoria de Gerente
        if turno == matutino or turno == vespertino:
            # turno matutino ou vespertino
            valor_percentual = 0.15
        else:
            # turno noturno
            valor_percentual = 0.10
    if cargo == operario:
        # Categoria de Operario
        if turno == matutino or turno == vespertino:
            # turno matutino ou vespertino
            valor_percentual = 0.14
        else:
            # turno noturno
            valor_percentual = 0.09
    return valor_percentual


def getSalarioFinal(valor_percentual, qtd_horas_trabalhadas):
    valor_hora_trabalhada = salario_base * valor_percentual
    salario_final = valor_hora_trabalhada * qtd_horas_trabalhadas
    return salario_final


def formatToReal(salario):
    return 'R$' + str(salario).replace('.', ',')


def root():
    dados_de_entrada = generalInput()
    print(dados_de_entrada)
    valor_percentual = getValorPercentual(dados_de_entrada[1], dados_de_entrada[2])
    salario_final = getSalarioFinal(valor_percentual, dados_de_entrada[3])
    output = 'Salario final: ' + formatToReal(salario_final)
    print(output)


# root code
root()
# end root code
