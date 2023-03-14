# 1) A empresa TECNOLOGIA LTDA deseja informatizar sua folha de pagamento, desenvolva
# um algoritmo que faça esse controle, para isso:
# a) Colete as seguintes informações:
# Nome;
# Quantidade de horas trabalhadas no mês;
# Turno de trabalho (M = Matutino, V = Vespertino e N = Noturno)
# Categoria (G = Gerente e O = Operário)
# b) Salve as informações dos funcionários em uma lista, não permitindo que sejam
# informados turnos e categorias inexistentes e não aceitar valores vazios e/ou nulos.
# c) Calcule o valor da hora trabalhada conforme a tabela a seguir.
# (Adote o valor de R$ 1.320,00 para o salário mínimo.)
# Categoria Turno Valor da hora trabalhada

# G N 10% do salário mínimo
# G M ou V 15% do salário mínimo
# O N 9% do salário mínimo
# O M ou V 14% do salário mínimo

# d) Calcule e mostre o salário de cada funcionário com base nas horas trabalhadas e
# no valor calculado para hora trabalhada de cada funcionário.

# ============================================================================================================

# nome = input(str('Nome: '))
# turno = input(str('Turno (M-Matutino, V-Vespertino ou N-Noturno): '))
# categoria = input(str('Categoria: (G-Gerente ou O-Operário): '))

salario_minimo = 1320
valor_hora_trabalhada = 0

nome = 'Caio'
turno = 'N'
categoria = 'G'
qtd_horas_trabalhadas = 2

lista = [nome, turno, categoria]

if categoria == 'G':
  if turno == 'M' or turno == 'V':
    valor_hora_trabalhada = salario_minimo * 0.15
    salario_final = valor_hora_trabalhada * qtd_horas_trabalhadas
  else:
    valor_hora_trabalhada = salario_minimo * 0.10
    salario_final = valor_hora_trabalhada * qtd_horas_trabalhadas
    
if categoria == 'O':
  if turno == 'M' or turno == 'V':
    valor_hora_trabalhada = salario_minimo * 0.14
    salario_final = valor_hora_trabalhada * qtd_horas_trabalhadas
  else:
    valor_hora_trabalhada = salario_minimo * 0.09
    salario_final = valor_hora_trabalhada * qtd_horas_trabalhadas

print('Salário Final do Funcionário: R$', salario_final)
    

