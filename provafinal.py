#1. Faça um programa que efetue a apresentação do valor da conversão
# em real (R$) de um valor lido em dólar (US$). Para isso, será
#necessário também ler o valor da cotação do dólar. (2,5pt)
dolar = float(input('Digite o valor em dolar: ')
cotacao = float('Qual a cotação do dia? ')
print(f'O valor em reais é {dolar*cotacao}')

#2. Faça um programa que leia um número e imprima uma das mensagens:
# "Maior do que 20", "Igual a 20"ou "Menor do que 20". (2,5pt)
num = float(input('Insira um número qualquer')
if num > 20: 
    print('Maior do que 20')
  if num = 20: 
    print('Igual a 20')
else
    print('Menor do que 20')

#3. Faça umprograma que leia um número inteiro e apresente o fatorial desse
# número.
# Ex.: o fatorial de 5 é igual a 5x4x3x2x1 = 120. (2,5pt)
num = int(input("Fatorial de: ") )
total=1
for n in range(1,num+1):
    total *= n
print(total)

#4. Faça um programa que permita:
# * ler um arquivo (licencas.dat) contendo dados de vários softwares (nome do software, número da licença);
# * buscar a licença de um software pelo nome;
# Os dados no arquivo (licencas.dat) estão organizados conforme:
# NOME_SOFTWARE;NUMERO_LICENCA
# NOME_SOFTWARE;NUMERO_LICENCA
# ...
with open('Programa.dat', 'a') as arquivos:
    while True:
        software =input('software: ')
        if software == 'sair':
            break
        licensa = input('Programa: ')
        arquivos.write(f'{software};{licensa}\n')
