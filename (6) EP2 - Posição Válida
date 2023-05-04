def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_ocupados = [[linha, coluna]]
    
    for espaco in range (1, tamanho):
        if orientacao == 'horizontal':
            prox = [linha, coluna + espaco]
        else:
            prox = [linha + espaco, coluna]

        lista_ocupados.append(prox)
    
    return lista_ocupados

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