def faz_jogada(tabuleiro, linha, coluna):
    jogada = tabuleiro[linha][coluna]

    if jogada == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    
    return tabuleiro