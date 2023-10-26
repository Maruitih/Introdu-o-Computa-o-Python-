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

## parâmetros para o método das congruências lineares:
m = 2**32
a = 22695477
c = 1
anterior = 42


# Continue aqui o seu programa ...
numJogadas= int(input("Digite o numero de jogadas \n"))
numJogadas2 = 0
jogadas = numJogadas
exponencial = 0
digito = 0
numAcertos = 0
p = 1
x = 0
while(numJogadas != numJogadas2):
    n1 = int(input("Pessoa 1 digite um numero \n"))
    n2 = int(input("Pessoa 2 digite um numero \n"))
    soman1 = 0
    soman2 = 0
    while(soman1==0):
        numdigitos = 100
        while(exponencial < 1):
            exponencial = n1//10** numdigitos
            numdigitos = numdigitos - 1
        numdigitos = numdigitos + 2
        exponencial = 0
        while(numdigitos > 0):
            digito = n1 // 10**(numdigitos - 1)
            soman1 = soman1 + digito
            n1 = n1 - digito*(10**(numdigitos - 1))
            numdigitos = numdigitos - 1
        if (soman1 > 9):
            n1 = soman1
            soman1= 0
    while(soman2==0):
        numdigitos = 100
        while(exponencial < 1):
            exponencial = n2//10** numdigitos
            numdigitos = numdigitos - 1
        numdigitos = numdigitos + 2
        exponencial = 0
        while(numdigitos > 0):
            digito = n2 // 10**(numdigitos - 1)
            soman2 = soman2 + digito
            n2 = n2 - digito*(10**(numdigitos - 1))
            numdigitos = numdigitos - 1
        if(soman2 > 9):
            n2 = soman2
            soman2 = 0
    if(soman1 == soman2):
        numAcertos = numAcertos + 1
    numJogadas2 = numJogadas2 + 1
afinidade = numAcertos/ numJogadas
pergunta = input("Deseja simular jogadas aleatorias (S/N)? \n")
if(pergunta =="S"):
    numJogadas2 = 0
    while(numJogadas2 != 10000):
        jogadas = numJogadas
        numJogadas2 = numJogadas2 + 1
        numAcertos2 = 0
        while(jogadas != 0):
            jogadas = jogadas - 1
            aleatorio1 = ((a * anterior + c) % m)
            anterior = aleatorio1
            aleatorio2 = ((a * anterior + c) % m)
            anterior = aleatorio2
            soman1 = 0
            soman2 = 0
            while(soman1==0):
                numdigitos = 100
                while(exponencial < 1):
                    exponencial = aleatorio1//10** numdigitos
                    numdigitos = numdigitos - 1
                numdigitos = numdigitos + 2
                exponencial = 0
                while(numdigitos != 0):
                    digito = aleatorio1 // 10**(numdigitos - 1)
                    soman1 = soman1 + digito
                    aleatorio1 = aleatorio1 - digito*(10**(numdigitos - 1))
                    numdigitos = numdigitos - 1
                if(soman1 > 9):
                    aleatorio1 = soman1
                    soman1 = 0
            while(soman2==0):
                numdigitos = 100
                while(exponencial < 1):
                    exponencial = aleatorio2//10** numdigitos
                    numdigitos = numdigitos - 1
                numdigitos = numdigitos + 2
                exponencial = 0
                while(numdigitos > 0):
                    digito = aleatorio2 // 10**(numdigitos - 1)
                    soman2 = soman2 + digito
                    aleatorio2 = aleatorio2 - digito*(10**(numdigitos - 1))
                    numdigitos = numdigitos - 1
                if(soman2 > 9):
                    aleatorio2 = soman2
                    soman2 = 0
            if(soman1 == soman2):
                numAcertos2 = numAcertos2 + 1
        if (numAcertos2 >= numAcertos):
            x = x + 1
    p = x / 10000
    afinidade = 1 - p
print("A afinidade de voces e de ", afinidade)
if((1/3)>afinidade>=0):
    print("A afinidade de voces e baixa. Que pena!")
if((2/3)>afinidade>=(1/3)):
    print("A afinidade de voces e mediana!")
if(afinidade>=(2/3)):
    print("Parabens! Voces tem uma bela afinidade!")
