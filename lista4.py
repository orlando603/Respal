import random
'''
Lista de Exercícios referentes a coleções em python
'''

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
def q01():
    lista = []
    for x in range(15):
        lista.append(random.randrange(100))
    print(lista)
    num = 0
    erro = True
    while erro == True:
        try:
            num = int(input('Digite um número a ser buscado: '))
            erro = False
        except:
            print('Informe um valor válido para inteiro!')
            erro = True
    try:
        print(f'Valor encontrado na posição: {lista.index(num)}')
    except ValueError:
        print('Valor não encontrado na lista')
    except:
        print('Erro desconhecido, contate o administrador do sistema!')


#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada.
def q02():
    lista = []
    for x in range(10):
        lista.append(chr(random.randrange(65,91)))
    cont = 0
    for letra in lista:
        print(f'{cont}: {letra}')
        cont+=1

#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
def q03():
    lista = []
    for x in range(15):
        lista.append(random.randrange(100))
    cont = 0
    for numero in lista:
        print(f'{cont}: {numero}\t{"PAR" if numero%2==0 else "IMPAR"}')



#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
def q04():
    lista = []
    
    for x in range(8):
        lista.append(random.randrange(10))
    cont = 0
    for numero in lista:
        print(f'{cont}: {numero}\t{"multiplo de 6" if numero%6==0 else "não é ultiplo de 6"}') 

  

#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
def q05():
    notas1 = []
    notas2 = []
    medias = []
    situacoes = []
    for c in range(15):
        notas1.append(random.randrange(0,11))
        notas2.append(random.randrange(0,11))
        medias.append((notas1[c] + notas2[c])/2)
        if medias[c] >= 6:
            situacoes.append('APROVADO')
        else:
            situacoes.append('REPROVADO')
    print('N1\tN2\tMED\tSITUACAO')
    for c in range(15):
        print(f'{notas1[c]}\t{notas2[c]}\t{medias[c]}\t{situacoes[c]}')

#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.
def q06():
    salario = []
    reajuste = []
    nv_salario = []
    for x in  range(20):
        salario.append(random.randrange(1000, 5000))
        reajuste.append((salario[x]*8)/100)
        nv_salario.append((salario[x]+reajuste[x]))
    print('SAL\tREAJ\tNVSAL')
    for x in range(20):
        print(f"{salario[x]}\t{reajuste[x]}\t{nv_salario[x]}")   
#7. Crie umprograma que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%
def q07():
    preço_c = []
    preço_v = []
    lucro = []
    for x in range(10):
        preço_c.append(float(random.randrange(100, 500)))
        preço_v.append(float(random.randrange(100, 1000)))
        lucro.append(preço_v[x]-preço_c[x])
        if lucro[x] < (lucro[x]*10)/100:
            print (f"{lucro[x]} < 10%")
        elif lucro[x] >=  (lucro[x]*10)/100 and lucro[x] <= (lucro[x]*20)/100: 
            print(f'10% <= {lucro[x]} <= 20%') 
        else:
            print(f'{lucro[x]} > 20%')     
    print('P_C\tP_V\tLUCRO')
    for x in range(10):
        print(f"{preço_c[x]}\t{preço_v[x]}\t{lucro[x]}")



#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.
def q08():
    estoque = {
        'cod ':'12' , 'quant' : '2', 'valor_c' : '35' , 'valor_v' : '70' , 'produto':'ferro'
        'cod ':'21' , 'quant' : '3', 'valor_c' : '40' , 'valor_v' : '80', 'produto':'aluminio'
        'cod ' : '13' , 'quant' : '4', 'valor_c' : '50.25' , 'valor_v' : '100.5', 'produto':'barras'
        'cod ' : '31' , 'quant' : '5', 'valor_c' : '20' , 'valor_v' : '6.75', 'produto':'cimento'
        'cod ' : '14' , 'quant' : '1', 'valor_c' : '30' , 'valor_v' : '70.65', 'produto':'manilha'
        'cod ' : '41' , 'quant' : '3', 'valor_c' : '1.50' , 'valor_v' : '7.50', 'produto':'ferro1'
        'cod ' : '15' , 'quant' : '7', 'valor_c' : '20' , 'valor_v' : '85.50', 'produto':'ferro2'
        'cod ' : '51' , 'quant' : '8', 'valor_c' : '5' , 'valor_v' : '120', 'produto':'ferro3'
        'cod ' : '16' , 'quant' : '9', 'valor_c' : '2.5' , 'valor_v' : '35', 'produto':'ferro4'
        'cod ' : '61' , 'quant' : '10', 'valor_c' : '0.5' , 'valor_v' : '45', 'produto':'ferro5'
        'cod ' : '17' , 'quant' : '2', 'valor_c' : '10' , 'valor_v' : '98', 'produto':'ferro6'
        'cod ' : '71' , 'quant' : '3', 'valor_c' : '20' , 'valor_v' : '65', 'produto':'ferro7'
        'cod ' : '18' , 'quant' : '5', 'valor_c' : '25' , 'valor_v' : '72.50', 'produto':'ferro8'
        'cod ' : '81' , 'quant' : '7', 'valor_c' : '60' , 'valor_v' : '36', 'produto':'ferro9'
        'cod ' : '19' , 'quant' : '8', 'valor_c' : '80' , 'valor_v' : '15.50', 'produto':'ferro10'
        'cod ' : '91' , 'quant' : '2', 'valor_c' : '1' , 'valor_v' : '12', 'produto':'estrutura1'
        'cod ' : '23' , 'quant' : '9', 'valor_c' : '0.75' , 'valor_v' : '10', 'produto':'estrutura1'
        'cod ' : '32' , 'quant' : '2', 'valor_c' : '50' , 'valor_v' : '150', 'produto':'estrutura2'
        'cod ' : '24' , 'quant' : '3', 'valor_c' : '30' , 'valor_v' : '60', 'produto':'estrutura3'
        'cod ' : '42' , 'quant' : '2', 'valor_c' : '65' , 'valor_v' : '30', 'produto':'estrutura4'
        'cod ' : '25' , 'quant' : '4', 'valor_c' : '2' , 'valor_v' : '20', 'produto':'estrutura5'
        'cod ' : '52' , 'quant' : '2', 'valor_c' : '30' , 'valor_v' : '160', 'produto':'estrutura6'
        'cod ' : '26' , 'quant' : '1', 'valor_c' : '150' , 'valor_v' : '500', 'produto':'estrutura7'
        'cod ' : '62' , 'quant' : '2', 'valor_c' : '25' , 'valor_v' : '70', 'produto':'estrutura8'
        'cod ' : '27' , 'quant' : '9', 'valor_c' : '100' , 'valor_v' : '250', 'produto':'estrutura9'
        'cod ' : '72' , 'quant' : '1', 'valor_c' : '36' , 'valor_v' : '65', 'produto':'estrutura10'
        'cod ' : '28' , 'quant' : '2', 'valor_c' : '25' , 'valor_v' : '95', 'produto':'estrutura1.1'
        'cod ' : '82' , 'quant' : '3', 'valor_c' : '21' , 'valor_v' : '85', 'produto':'estrutura1.2'
        'cod ' : '29' , 'quant' : '4', 'valor_c' : '20' , 'valor_v' : '45', 'produto':'estrutura1.3'
        'cod ' : '92' , 'quant' : '5', 'valor_c' : '9' , 'valor_v' : '650', 'produto':'estrutura1.4'
    }
    print(estoque)
q08() 
#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#um vetor e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.
