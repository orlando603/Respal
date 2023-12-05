#1. Faça um programa que efetue a apresentação do valor da conversão
# em real (R$) de um valor lido em dólar (US$). Para isso, será
#necessário também ler o valor da cotação do dólar. (2,5pt)
def q01():

    print('Conversor de dolar para real')
    valor = float(input('Digite o valor em dolar($): '))
    cotaçao = float(input('informe o valor de cotação dolar/dia($): '))
    print(f'O valor da coverção em reais(R$) é: {valor*cotaçao}')






#2. Faça um programa que leia um número e imprima uma das mensagens:
# "Maior do que 20", "Igual a 20"ou "Menor do que 20". (2,5pt)
def q02():

    num = float(input(' Digite um numero: '))
    if num > 20:
        print('O numero informado é maior do que 20')
    if num == 20:
        print('O numero informado é igual a 20')   
    if num  < 20:
        print('O número informado é menor do que 20')     

#3. Faça umprograma que leia um número inteiro e apresente o fatorial desse
# número.
# Ex.: o fatorial de 5 é igual a 5x4x3x2x1 = 120. (2,5pt)
def q03():
    
    
#4. Faça um programa que permita:
# * ler um arquivo (licencas.dat) contendo dados de vários softwares (nome do software, número da licença);
# * buscar a licença de um software pelo nome;
# Os dados no arquivo (licencas.dat) estão organizados conforme:
# NOME_SOFTWARE;NUMERO_LICENCA
# NOME_SOFTWARE;NUMERO_LICENCA
# ...
def q04():
    with open('Programa.dat', 'a') as arquivos:
        while True:
            software =input('software: ')
            if software == 'sair':
                break
            licensa = input('Programa: ')
            arquivos.write(f'{software};{licensa}\n')
q02()