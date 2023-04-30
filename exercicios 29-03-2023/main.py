from termcolor import colored
import time

menu_header = colored('Menu principal \n', 'cyan')
option_1 = '1 - Registrar Notas de um aluno \n'
option_2 = '2 - Calcular média final dos alunos \n'
menu = menu_header + option_1 + option_2
valid_options = ['1', '2']

options_data = [
    {
        'id': '1',
        'function': 'register_notes()'
    },
    {
        'id': '2',
        'function': 'calc_media()'
    },
]


def c_print(value, color):
    print(colored(value, color))


def validate(valid_inputs: list or bool, text: str):
    print(text)
    while True:
        value = input('\t => ')
        if value == '':
            c_print('Por favor, informe uma opção', 'red')
        elif valid_inputs:
          if not value in valid_inputs:
              c_print('Por favor, informe uma opção válida', 'red')
        else:
            c_print('Sucesso', 'green')
            break
    return value


def register_notes():
    c_print('\tMenu -> 1', 'blue')
    name = input('Insira o nome do aluno: ')
    nota_1 = input('Informe a Primeira nota: ')
    nota_2 = input('Informe a Segunda nota: ')
    nota_3 = input('Informe a Terceira nota: ')


def calc_media():
    print('media')


def root():
    print(menu)
    while True:
        selected_option = validate(['1', '2'], 'Informe a opção desejada')
        print(selected_option)
        for option in options_data:
            if selected_option == option['id']:
                print('entrou')
                eval(option['function'])
        break


root()
