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

#Preenche Frota
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicao_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in frota:
        frota[nome_navio] = []
    
    frota[nome_navio].append(posicao_navio)

    return frota