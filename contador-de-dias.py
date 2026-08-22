from datetime import date, timedelta
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
    ).strip().upper()

    if pergunta == 'F':
        try:
            quantos = int(input('Quantos dias você quer calcular no futuro? '))
        except ValueError:
            print('Digite um número válido.')
            continue

        futuro = hoje + timedelta(days=quantos)

        print('calculando...')
        sleep(2)
        print(
            f'Hoje é {hoje.strftime("%d/%m/%Y")} '
            f'e daqui a {quantos} dias será {futuro.strftime("%d/%m/%Y")}.'
        )

    elif pergunta == 'P':
        try:
            quantos = int(input('Quantos dias você quer calcular no passado? '))
        except ValueError:
            print('Digite um número válido.')
            continue

        passado = hoje - timedelta(days=quantos)
        
        print('calculando...')
        sleep(2)
        print(
            f'Hoje é {hoje.strftime("%d/%m/%Y")} '
            f'e {quantos} dias atrás foi {passado.strftime("%d/%m/%Y")}.'
        )

    else:
        print('Por favor, informe um valor válido: F para futuro ou P para passado.')

    deseja = input('\nDeseja sair? (S/N): ').strip().upper()

    if deseja == 'S':
        print('Programa encerrado!')
        break