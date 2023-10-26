"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Henrique Maruiti
  NUSP : 12610243
  Turma: 04
  Prof.: Kelly Rosa Braghetto

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort

  """
  
# Funções que devem ser implementadas sem alteracao de assinatura:

# Funcao 1 - Quantidade de pontos na borda
def pontosNaBorda(v0, v1, v2):
    quantidade = 0
    for i in range(0,1):
        if v0[i] - v1[i] == 0:
            if i == 0:
                conta = v0[1] - v1[1]
            if i == 1:
                conta = v0[0] - v1[0]
            if conta < 0:
                conta = conta * (-1)
            pontos = conta
            quantidade = quantidade + pontos
        else:
            a = v0[0] - v1[0]
            b = v0[1] - v1[1]
            if a < 0:
                a = a *(-1)
            if b < 0:
                b = b*(-1)

            while b != 0:
                resto = a%b
                a = b
                b = resto
            quantidade = quantidade + a

        if v1[i] - v2[i] == 0:
            if i == 0:
                conta = v1[1] - v2[1]
            if i == 1:
                conta = v1[0] - v2[0]
            if conta < 0:
                conta = conta * (-1)
            pontos = conta
            quantidade = quantidade + pontos
        else:
            a = v1[0] - v2[0]
            b = v1[1] - v2[1]
            if a < 0:
                a = a *(-1)
            if b < 0:
                b = b*(-1)

            while b != 0:
                resto = a%b
                a = b
                b = resto
            quantidade = quantidade + a

        if v2[i] - v0[i] == 0:
            if i == 0:
                conta = v2[1] - v0[1]
            if i == 1:
                conta = v2[0] - v0[0]
            if conta < 0:
                conta = conta * (-1)
            pontos = conta
            quantidade = quantidade + pontos
        else:
            a = v2[0] - v0[0]
            b = v2[1] - v0[1]
            if a < 0:
                a = a *(-1)
            if b < 0:
                b = b*(-1)
            while b != 0:
                resto = a%b
                a = b
                b = resto
            quantidade = quantidade + a

    # v0, v1, v2 são coordenadas dos vértices de um triângulo
    return quantidade

# Funcao 2 - Soma pontos na borda
def somaPontosNaBorda(alienigenas):
    quantidade = 0
    numero_alienigena = len(alienigenas)
    for i in range (0,numero_alienigena):
        lista1 = alienigenas
        lista = alienigenas[i]
        quantidade = quantidade + (pontosNaBorda(lista[0], lista[1], lista[2]))
        alienigenas = lista1 
    # alienigenas é uma lista de triângulos
    return quantidade

# Funcao 3 - Ponto interno
def pontoInterno(ponto, v0, v1, v2):
    # ponto é a coordenada do ponto de uma munição
    v1a = v1[0] - v0[0]
    v1b = v1[1] - v0[1]
    v1_ = [v1a, v1b]
    v2a = v2[0] - v0[0]
    v2b = v2[1] - v0[1]
    v2_ = [v2a, v2b]
    a = (det(ponto,v2_) - det(v0, v2_))/ det(v1_, v2_)
    b = -(det(ponto,v1_) - det(v0, v1_))/ det(v1_,v2_)
    # se ponto for interno:
    if a > 0 and b > 0 and a + b < 1:
        return True
    # caso contrário:
    else:
        return False

# Funcao 4 - Limite de busca
def limitesDeBusca(v0, v1, v2):
    for i in range(0,2):
        if v0[i] >= v1[i] and v0[i] >= v2[i] and v2[i] >=v1[i]:
            if i == 0:
                x_max = v0[0]
                x_min = v1[0]
            else:
                y_max = v0[1]
                y_min = v1[1]
        if v0[i] >= v1[i] and v0[i] >= v2[i] and v1[i] >=v2[i]:
            if i == 0:
                x_max = v0[0]
                x_min = v2[0]
            else:
                y_max = v0[1]
                y_min = v2[1] 
        if v1[i] >= v0[i] and v1[i] >= v2[i] and v0[i] >= v2[i]:
            if i == 0:
                x_max = v1[0]
                x_min = v2[0]
            else:
                y_max = v1[1]
                y_min = v2[1]
        if v1[i] >= v0[i] and v1[i] >= v2[i] and v2[i] >= v0[i]:
            if i == 0:
                x_max = v1[0]
                x_min = v0[0]
            else:
                y_max = v1[1]
                y_min = v0[1]
        if v2[i] >= v1[i] and v2[i] >= v0[i] and v1[i] >= v0[i]:
            if i == 0:
                x_max = v2[0]
                x_min = v0[0]
            else:
                y_max = v2[1]
                y_min = v0[1]
        if v2[i] >= v1[i] and v2[i] >= v0[i] and v0[i] >= v1[i]:
            if i == 0:
                x_max = v2[0]
                x_min = v1[0]
            else:
                y_max = v2[1]
                y_min = v1[1]
    # v0, v1, v2 são coordenadas dos vértices de um triângulo
    return x_min, y_min, x_max, y_max

# Funcao 5 - Pontos internos
def pontosInternos(v0, v1, v2):
    # v0, v1, v2 são coordenadas dos vértices de um triângulo
    limite = [limitesDeBusca(v0, v1, v2)]
    x_min = limite[0][0]
    y_min = limite[0][1]
    x_max = limite[0][2]
    y_max = limite[0][3]
    quantidade = 0
    while x_min <= x_max:
        limite_0 = y_min
        while y_min <= y_max:
            ponto = [x_min, y_min]
            resposta = pontoInterno(ponto, v0, v1, v2)
            y_min += 1
            if resposta == True:
                quantidade = quantidade + 1
        x_min += 1
        y_min = limite_0
    return quantidade

# Funcao 6 - Soma pontos internos
def somaPontosInternos(alienigenas):
    quantidade = 0
    numero_alienigena = len(alienigenas)
    for i in range (0,numero_alienigena):
        lista1 = alienigenas
        lista = alienigenas[i]
        quantidade = quantidade + (pontosInternos(lista[0], lista[1], lista[2]))
        alienigenas = lista1
    # alienigenas é uma lista de triângulos
    return quantidade

def main():
    alienigenas = []
    n = int(input("Quantidade de alienigenas:\n"))
    for i in range(0,n):
        alienigenas.append( leAlienigena(i) )
    pergunta(alienigenas, n)
    # Continue aqui o seu programa para testar as funcoes acima...

def leAlienigena(numero_alienigena):
    coordenadas = input("Alienigena %d:\n" %(numero_alienigena))
    # converte a string lida em uma lista de inteiros
    coordenadas = coordenadas.split()
    for i in range(0,6):
        coordenadas[ i ] = int( coordenadas[ i ] )
        # separa as três coordenadas dos vértices do alienígena
    v0 = [ coordenadas[0], coordenadas[1] ]
    v1 = [ coordenadas[2], coordenadas[3] ]
    v2 = [ coordenadas[4], coordenadas[5] ]
    return v0, v1, v2

def det(m, n):
    determinante = ((m[0]*n[1]) - (m[1]*n[0]))
    return determinante

def pergunta(alienigenas, n):
    resposta = int(input("Digite a funcao que deseja testar:\n"))
    if (resposta == 1):
        numero_alienigena = int (input("Numero do alienigena:\n"))
        lista = alienigenas[numero_alienigena]
        quantidade = (pontosNaBorda(lista[0], lista[1], lista[2]))
        print("Quantidade de pontos na borda: ", quantidade)
        pergunta(alienigenas, n)
    if (resposta == 2):
        quantidade = somaPontosNaBorda(alienigenas)
        print("Soma de pontos na borda:", quantidade)
        pergunta(alienigenas, n)
    if (resposta == 3):
        numero_alienigena = int (input("Numero do alienigena:\n"))
        lista = alienigenas[numero_alienigena]
        print("Coordenadas do alienigena:",(lista[0][0], lista[0][1]), (lista[1][0], lista[1][1]), (lista[2][0], lista[2][1]))
        coordenadas = input("Coordenadas do ponto: ")
        coordenadas = coordenadas.split()
        coordenadas[0] = int (coordenadas[0])
        coordenadas[1] = int (coordenadas[1])
        ponto = [coordenadas[0],coordenadas[1]]
        resposta1 = pontoInterno(ponto, lista[0], lista[1], lista[2])
        if resposta1 == True:
            print("Ponto interno ao triangulo!\n")
        else:
            print("Ponto nao interno ao triangulo!\n")
        pergunta(alienigenas,n)
    if (resposta == 4):
        numero_alienigena = int (input("Numero do alienigena: \n"))
        lista = alienigenas[numero_alienigena]
        limite = (limitesDeBusca(lista[0], lista[1], lista[2]))
        print("Os limites são:",(limite[0],limite[1]) ,"e",(limite[2],limite[3]))
        pergunta(alienigenas,n)
    if (resposta == 5): 
        numero_alienigena = int(input("Numero do alienigena:\n"))
        lista = alienigenas[numero_alienigena]
        quantidade = (pontosInternos(lista[0], lista[1], lista[2]))
        print("Quantidade de pontos internos: ", quantidade)
        pergunta(alienigenas,n)
    if (resposta == 6):
        quantidade = somaPontosInternos(alienigenas)
        print("Soma de pontos internos:", quantidade)
        pergunta(alienigenas,n)
# NAO REMOVA AS LINHAS A SEGUIR
if __name__ == '__main__':
    main()
