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
  Prof.: Kelly Rosa

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort

"""
  
###############################################################################
# Funções Adicionais 
# Se quiser, escreva aqui funções adicionais para ajudar na resolução do EP.
###############################################################################

### ESCREVA AQUI AS FUNÇÕES ADICIONAIS
    
  
###############################################################################
# Funções Obrigatórias
# Devem ser implementadas sem alterar os parâmetros e tipo do valor de retorno.
###############################################################################

def obtemPalavrasProximas(palavra, vocabulario):
    """ Devolve uma lista de palavras que diferem da palavra do parâmetro 
    em apenas uma letra.
    Na lista, primeiro devem aparecer as palavras que diferem na primeira
    letra à esquerda, depois as que diferem na segunda letra à esquerda, e 
    assim por diante.
    As palavras da lista devolvida devem existir na lista de palavras do 
    vocabulário passada como parâmetro para a função.
    
    Parâmetros:
    palavra -- a palavra da qual se deseja encontrar as palavras próximas
    vocabulario -- lista das palavras do vocabulário"""    
    
    ### ESCREVA AQUI O CORPO DA FUNÇÃO
    lista = open(vocabulario)
    proximas = []
    proximas1 = ""
    proximas2 = ""
    proximas3 = ""
    proximas4 = ""
    proximas5 = ""
    proximas0 = ""
    for i in range(1,7370):
        i = 0
        palavras = lista.readline()
        palavras = palavras.strip()
        if palavras != palavra and len(palavras) == len(palavra):
            for i in range (i,len(palavra)):
                inicial = palavra[0:i]
                final = palavra[i+1:len(palavra)]
                i += 1
                if(palavras.find(inicial.strip()) == 0):
                        ordem= palavras.find(final.strip())
                        if ordem == 1 and palavra[len(palavra)-1] == palavras[len(palavra)-1]:
                            proximas1 = proximas1 + palavras +" "
                        if ordem == 2:
                            proximas2 = proximas2 + palavras +" "
                        if ordem == 3:
                            proximas3 = proximas3 + palavras +" "
                        if ordem == 4:
                            proximas4 = proximas4 + palavras +" "
                        if ordem == 5:
                            proximas5 = proximas5 + palavras +" "
                        if ordem == 0 and palavras[0] == palavra[0]:
                            proximas0 = proximas0 + palavras +" "
    proximas = proximas1 + proximas2 + proximas3 + proximas4 + proximas5 + proximas0
    proximas = proximas.strip(" ")
    proximas = proximas.split(" ")
    if proximas == ['']:
        proximas=[]
    return proximas  # lista das palavras próximas

def criaArvoreDeBusca(inicio, fim, vocabulario):
    """ Devolve uma lista com os nós da árvore de busca de caminho entre as
    palavras inicio e fim. Cada nó é uma lista contendo uma palavra e a 
    posição do seu nó pai. Portanto, a função devolve uma lista de listas.
    Os nós possuem apenas palavras existentes na lista de palavras do 
    vocabulário passada no parâmetro.
    
    Parâmetros:
    inicio -- palavra de início do caminho a ser buscado
    fim -- palavra de fim do caminho a ser buscado
    vocabulario -- lista das palavras do vocabulário"""
    
    ### ESCREVA AQUI O CORPO DA FUNÇÃO
    ### VOCÊ DEVE USAR A obtemPalavrasProximas() NA IMPLEMENTAÇÃO
    busca = ""
    i = 0
    no = []
    pai = [inicio +", -1"]
    no.append(pai)
    b = 0
    while fim != busca:
        lista = obtemPalavrasProximas(inicio, vocabulario)
        if lista ==[]:
            return no
        if i != len(lista):
            busca = lista[i]
            b = str(b)
            a = str(", " + b)
            no1 = [lista[i] + a ]
            no.append(no1)
            i = i + 1
        else:
            i = 0
            b = int (b)
            b = b + 1
    return no

def main():
    """Esta função faz a interação com o usuário (ou seja, cuida da entrada
    e saída de dados). Ela possibilita a execução de testes sobre as três 
    funções obrigatórias -- obtemPalavrasProximas(), criaArvoreDeBusca(), 
    obtemCaminho() -- do EP4."""
    
    # Nome do arquivo de vocabulário
    nome_arquivo = "./vocabulario.txt"
    pergunta(nome_arquivo)

def pergunta(vocabulario):
    ### ESCREVA AQUI O CORPO DA FUNÇÃO
    resposta = int(input("Digite a opcao:\n"))
    if resposta == 1:
        palavra = input("Digite uma palavra:\n")
        print("Palavras proximas de",palavra,":", obtemPalavrasProximas(palavra, vocabulario))
        pergunta(vocabulario)
    if resposta == 2:
        inicio = input("Digite a palavra de inicio: ")
        fim = input("Digite a palavra de fim: ")
        arvore = criaArvoreDeBusca(inicio, fim, vocabulario)
        print("Quantidade de nos da arvore :",len(arvore))
        print("Arvore: ",arvore)
        pergunta(vocabulario)
    return
              
                
# NÃO REMOVA AS LINHAS A SEGUIR
if __name__ == '__main__':
    main()
