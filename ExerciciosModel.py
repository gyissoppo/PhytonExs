import this


def exercicio01():
    A = 10
    B = 20
    msg = 'antes da troca A = {}, B = {}'.format(A,B)
    aux = A
    A = B
    B = aux
    msg = msg +'\nDepois da troca: A= {}, B = {}'.format(A,B)
    return msg

def exercicio02():
    print('digite o numero que voce deseja saber o antecessor')
    this.num3 = int(input())#entrada de dados
    print('o antecessor é {}'.format(this.num3 - 1))
    msgs = 'obrigado'
    return msgs

#jeito alternativo para resolver o ex: return 'o antecessor é {}'.format(num1-1)

def exercicio03():
    print('digite o valor da base:')
    this.base = float(input())
    print('digite o valor da altura:')
    this.altura = float(input())
    print('o valor da area do seu retangulozinho é de {}'.format(this.base*this.altura))
    msgs = 'obrigado'
    return msgs

def exercicio04():
    print('escreva sua idade em anos, meses e dias.')
    print('anos:')
    this.ano = int(input())
    print('meses:')
    this.mes = int(input())
    print('dias:')
    this.dia = int(input())
    print('sua idade em dias é {}'.format(this.ano * 365 + this.mes * 30 + this.dia))
    msgs = 'obrigado'
    return msgs

def exercicio05():
    print('total de votos válidos:')
    this.valido = int(input())
    print('total de votos em branco:')
    this.branco = int(input())
    print('total de votos nulos:')
    this.nulo = int(input())
    total = this.valido + this.nulo + this.branco
    totalV = this.valido / total
    totalB = this.branco / total
    totalN = this.nulo / total
    print('total de eleitores: {}'.format(total))
    print('percentual de votos válidos: {}%'.format(totalV * 100))
    print('percentual de votos em branco: {}%'.format(totalB * 100))
    print('percentual de votos nulos: {}%'.format(totalN * 100))
    msgs = 'obrigado'
    return msgs

def exercicio06():
    print('digite seu salário mensal atual:')
    salario = float(input())
    print('digite o percentual do reajuste:')
    print('favor nao digitar %')
    reajuste = float(input())
    salarioR = reajuste / 100 * salario
    print('seu salário com o reajuste é de R$ {}'.format(salarioR + salario))
    msgs = 'obrigado'
    return msgs

def exercicio07():
    print('digite o valor do custo de fabrica do carro:')
    fabrica = float(input())
    valor = fabrica + fabrica * 0.28 + fabrica * 0.45
    print('o custo final ao conasummidor é de R$ {}'.format(valor))
    msgs = 'obrigado'
    return msgs

def exercicio08():
    print('digite a priemieira nota:')
    nota1 = float(input())
    print('digite a segunda nota:')
    nota2 = float(input())
    print('digite a terceira nota:')
    nota3 = float(input())
    media = (nota1 + nota2 + nota3) / 3
    print('a media entre as três notas é de {}'.format(media))
    msgs = 'obrigado'
    return msgs

def exercicio09():
    print('quantidade de maçãs compradas:')
    maca = int(input())
    if maca <= 11:
        valor = 1.30
    else:
        valor = 1
    print('valor total: R$ {}'.format(maca * valor))
    msgs = 'obrigado'
    return msgs

def exercicio10():
    valor0 = 0
    print('valor 1')
    valor1 = float(input())
    print('valor 2')
    valor2 = float(input())
    print('valor 3')
    valor3 = float(input())
    print('valor 4')
    valor4 = float(input())
    print('valor 5')
    valor5 = float(input())
    print('valor 6')
    valor6 = float(input())
    print('valor 7')
    valor7 = float(input())
    print('valor 8')
    valor8 = float(input())
    print('valor 9')
    valor9 = float(input())
    print('valor 10')
    valor10 = float(input())

    if valor1 < 0:
        valor1 = valor0
    else:
        valor1 = valor1

def exercicio11():
    print('salário fixo: ')
    salario = float(input())
    print('valor das vendas: ')
    vendas = float(input())
    if vendas <= 1500:
        comissao = vendas * 0.03
    else:
        vendas1 = vendas - 1500
        comissao = vendas1 * 0.05 + 45
    print('o salário total é de R$ {}'.format(comissao + salario))
    msgs = 'obrigado'
    return msgs

def exercicio12():
    print('digite o número da sua conta: ')
    conta = int(input())
    print('digite o saldo da sua conta: ')
    saldo = int(input())
    print('digite o debito: ')
    debito = float(input())
    print('digite o credito: ')
    credito = float(input())
    saldo1 = saldo - debito + credito
    print('seu saldo atual é de R$ {}'.format(saldo1))
    if saldo1 >= 0:
        return 'saldo positivo'
    else:
        return 'saldo negativo'

    msgs = 'obrigado'
    return msgs

def exercicio13():
    print('digite um numero de 1 a 10')
    num = int(input())
    if num > 10:
        print('digite um numero de 1 a 10')
    else:
        print('{} x 1 = {}'.format(num, num * 1))
        print('{} x 2 = {}'.format(num, num * 2))
        print('{} x 3 = {}'.format(num, num * 3))
        print('{} x 4 = {}'.format(num, num * 4))
        print('{} x 5 = {}'.format(num, num * 5))
        print('{} x 6 = {}'.format(num, num * 6))
        print('{} x 7 = {}'.format(num, num * 7))
        print('{} x 8 = {}'.format(num, num * 8))
        print('{} x 9 = {}'.format(num, num * 9))
        print('{} x 10 = {}'.format(num, num * 10))
    msgs = 'obrigado'
    return msgs

def exercicio14():
    msgs = 'obrigado'
    return msgs

def exercicio15():
    msgs = 'obrigado'
    return msgs

def exercicio16():
    msgs = 'obrigado'
    return msgs

def exercicio17():
    msgs = 'obrigado'
    return msgs

def exercicio18():
    msgs = 'obrigado'
    return msgs

def exercicio19():

    msgs = 'obrigado'
    return msgs

def exercicio20():
    msgs = 'obrigado'
    return msgs