import random
import colorama
colorama.init(autoreset = True)

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

#Posicionando Frota
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

#Lista de posições possíveis
pos_possiveis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

index = 0
while index != len(navios_posicionar):
    
    tipo_navio = navios_posicionar[index]
    tamanho = dicio_tamanhos[tipo_navio]

    print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(tipo_navio, tamanho))

    linha = input('Linha: ')
    while linha not in pos_possiveis:
        print(colorama.Fore.RED + 'Linha inválida!')
        linha = input('Linha: ')

    linha = int(linha)

    coluna = input('Coluna: ')
    while coluna not in pos_possiveis:
        print(colorama.Fore.RED + 'Coluna inválida!')
        coluna = input('Coluna: ')

    coluna = int(coluna)

    if tipo_navio != 'submarino':
        orientacao = input('[1] Vertical [2] Horizontal > ')
    
        while orientacao not in ['1', '2']:
            print(colorama.Fore.RED + 'Orientação Inválida!')
            orientacao = input('[1] Vertical [2] Horizontal > ')

        orientacao = int(orientacao)

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
        print(colorama.Fore.RED + 'Esta posição não está válida!')

#Jogadas do jogador
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

#Tabuleiro do jogador
tabuleiro_jogador = posiciona_frota(frota)

#Tabuleiro do oponente
tabuleiro_oponente = posiciona_frota(frota_oponente)

#Listas de jogadas
ja_jogado = []
ja_jogou_oponente = []

#Loop do jogo
jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    #Jogadas possíveis
    nao_jogou = True

    while nao_jogou:

        linha = input('Digite a linha que deseja atacar: ')
        while linha not in pos_possiveis:
            print(colorama.Fore.RED + 'Linha inválida!')
            linha = input('Digite a linha que deseja atacar: ')
    
        linha = int(linha)

        coluna = input('Digite a coluna que deseja atacar: ')
        while coluna not in pos_possiveis:
            print(colorama.Fore.RED + 'Coluna inválida!')
            coluna = input('Digite a coluna que deseja atacar: ')
    
        coluna = int(coluna)

        ataque = [linha, coluna]
        if ataque in ja_jogado:
            print(colorama.Fore.RED + 'A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha, coluna))
        else:
            ja_jogado.append(ataque)
            nao_jogou = False
    
    #Atualiza o tabuleiro do oponente
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == len(navios_posicionar):
        print(colorama.Fore.GREEN + 'Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    
    #Jogadas do oponente
    else:
        nao_jogou_oponente = True

        while nao_jogou_oponente:
            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)

            ataque = [linha_oponente, coluna_oponente]

            if ataque not in ja_jogou_oponente:
                ja_jogou_oponente.append(ataque)
                nao_jogou_oponente = False
    
        print(colorama.Fore.CYAN + 'Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_oponente, coluna_oponente))

        #Atualiza o tabuleiro do jogador
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

        if afundados(frota, tabuleiro_jogador) == len(navios_posicionar):
            print(colorama.Fore.RED + 'Xi! O oponente derrubou toda a sua frota =(')
            jogando = False