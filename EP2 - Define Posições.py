def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_ocupados = [[linha, coluna]]
    
    for espaco in range (1, tamanho):
        if orientacao == 'horizontal':
            prox = [linha, coluna + espaco]
        else:
            prox = [linha + espaco, coluna]

        lista_ocupados.append(prox)
    
    return lista_ocupados