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