############## Juntando todas as funções feitas até agora ##############

#Define posições
def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_ocupados = [[linha, coluna]]
    
    for espaco in range (1, tamanho):
        if orientacao == 'horizontal':
            prox = [linha, coluna + espaco]
        else:
            prox = [linha + espaco, coluna]

        lista_ocupados.append(prox)
    
    return lista_ocupados

#Preenche frota
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicao_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in frota:
        frota[nome_navio] = []
    
    frota[nome_navio].append(posicao_navio)

    return frota

#Faz jogada
def faz_jogada(tabuleiro, linha, coluna):
    jogada = tabuleiro[linha][coluna]

    if jogada == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    
    return tabuleiro

#Posiciona frota
def posiciona_frota(frota):
    tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    for tipo_navio, listas_posicoes in frota.items():
        for navio in listas_posicoes:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
    
    return tabuleiro

#Quantas embarcações afundadas
def afundados(frota, tabuleiro):
    afundou = 0

    for tipo_navio, lista_posicoes in frota.items():
        for navio in lista_posicoes:
            esta_afundado = True
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] != 'X':
                    esta_afundado = False
            
            if esta_afundado == True:
                afundou += 1
    
    return afundou

#Posição Válida
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    tabuleiro = posiciona_frota(frota)
    posicao_ocupada = define_posicoes(linha, coluna, orientacao, tamanho)
    
    for posicao in posicao_ocupada:
        linha = posicao[0]
        coluna = posicao[1]
        if linha > 9 or coluna > 9:
            return False
        elif tabuleiro[linha][coluna] == 1:
            return False

    return True

############## Comaçando o código do exercício ##############

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

navios_posicionar = ["porta-aviões", "navio-tanque", "navio-tanque", "contratorpedeiro", "contratorpedeiro", "contratorpedeiro", "submarino", "submarino", "submarino", "submarino"]

dicio_tamanhos = {
    "porta-aviões": 4,
    "navio-tanque": 3,
    "contratorpedeiro": 2,
    "submarino": 1,
}

index = 0
while index != len(navios_posicionar):
    
    tipo_navio = navios_posicionar[index]
    tamanho = dicio_tamanhos[tipo_navio]

    print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(tipo_navio, tamanho))

    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))

    if tipo_navio != 'submarino':
        orientacao = int(input('[1] Vertical [2] Horizontal > '))
        if orientacao == 1:
            orientacao = 'vertical'
        else:
            orientacao = 'horizontal'
        
    else:
        orientacao = 'vertical'
    
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if posicao_valida(frota, linha, coluna, orientacao, tamanho) == True:
        frota = preenche_frota(frota, tipo_navio, linha, coluna, orientacao, tamanho)
        index += 1
    else:
        print('Esta posição não está válida!')

print(frota)