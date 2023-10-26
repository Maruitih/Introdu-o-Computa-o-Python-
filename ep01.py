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
  Turma: 4
  Prof.: Kelly Rosa Braghetto

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort

  """

# O trecho abaixo sorteia um número inteiro no intervalo [1,20]
import random
semente = int(input("Digite a semente do sorteio: "))
random.seed(semente)
numero_sorteado = random.randint(1,20)

# Continue aqui o seu programa ...
#Mensagem do exemplo
print("Escolhi um inteiro entre 1 e 20. Adivinhe-o!") 
#Estabelecendo o funcionamento com base no numero de tentativas
numero_tentativas = 1
while numero_tentativas <= 5:
  tentativas = int(input("Seu chute: "))
  #Condicionais para estabelecer o funcionamento das mensagens
  if tentativas == numero_sorteado:
    print("Legal, acertou na tentativa",numero_tentativas)
    numero_tentativas = numero_tentativas + 6
  if tentativas < numero_sorteado:
    print("Chutou baixo")
  if tentativas > numero_sorteado:
    print("Chutou alto")
  if tentativas % 2 == 0:
    if numero_sorteado % 2 == 1:
      print("Tente um impar")
  if tentativas % 2 == 1:
    if numero_sorteado % 2 == 0:
      print("Tente um par")
  numero_tentativas = numero_tentativas + 1
if numero_tentativas == 6:
  print("Tentativas esgotadas!")
  print("O escolhido foi o",numero_sorteado)
