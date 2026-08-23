from datetime import date, timedelta
from babel.dates import format_date
from time import sleep

sleep(1)
print('CALCULADORA DE DIAS')
print('Calcula dias futuros ou passados com base na data atual')
sleep(1)

hoje = date.today()

while True:

    pergunta = input(
        '\nVocê quer calcular dias futuros ou passados? '
        '(F/P): '
    ).strip()[0].upper()

    if pergunta == 'F':
        try:
            quantos = int(input('Quantos dias você quer calcular no futuro? '))
        except ValueError:
            print('Digite um número válido.')
            continue

        futuro = hoje + timedelta(days=quantos)
        dia_da_semana_futuro = format_date(futuro, format="EEEE", locale='pt_BR')


        print('calculando...')
        sleep(2)
        print(
            f'Hoje é {hoje.strftime("%d/%m/%Y")} '
            f'e daqui a {quantos} dias será {futuro.strftime("%d/%m/%Y")} - {dia_da_semana_futuro}.'
        )

    elif pergunta == 'P':
        try:
            quantos = int(input('Quantos dias você quer calcular no passado? '))
        except ValueError:
            print('Digite um número válido.')
            continue

        passado = hoje - timedelta(days=quantos)
        dia_da_semana_passado = format_date(passado, format="EEEE", locale='pt_BR')

        
        print('calculando...')
        sleep(2)
        print(
            f'Hoje é {hoje.strftime("%d/%m/%Y")} '
            f'e {quantos} dias atrás foi {passado.strftime("%d/%m/%Y")} - {dia_da_semana_passado}.'
        )

    else:
        print('Por favor, informe um valor válido: F para futuro ou P para passado.')

    
    deseja = str(input('\nDeseja sair? (S/N): ')).strip()[0].upper()

    
    if deseja != 'N':
        print('Programa encerrado!')
        break
