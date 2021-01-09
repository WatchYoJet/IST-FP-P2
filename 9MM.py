# Pedro Maria Eustaquio Vaz Pereira ist198962
# ----------------------------------TAD-Posicao--------------------------------#
#A interpretacao interna deste TAD foi escolhida tendo em conta a sua
#representacao externa desta forma, e facil de entender as posicoes e
#torna-se mais logico como o programa funciona. Assim, esta interpretacao foi
#feita para evitar uma certa confusao de interpretacao e para se tornar mais
#facil a funcao cria_copia_posicao
#
#interpretacao interna -> 'a1'
#
#cria_posicao: str x str -> posicao
#cria_copia_posicao:posicao -> posicao
#obter_pos_c:posicao -> str
#obter_pos_l:posicao -> str
#eh_posicao:universal -> booleano
#posicoes_iguais:posicao x posicao -> booleano
#posicao_para_str:posicao -> str
#obter_posicoes_adjacentes: posicao -> tuplo de posicoes
# -----------------------------------------------------------------------------#
def cria_posicao(col, lin):  #construtor
    """
    :argumento col: str 
    :argumento lin: str 
    :return: posicao 
    Recebe duas strings, indicando a sua coluna e a linha,
    e retorna a sua posicao tendo em conta a sua interpretacao interna.
    Se os argumentos nao forem validos, a funcao retorna com um ValueError
    """
    if col in ("a", "b", "c") and lin in ("1", "2", "3"):
        return col + lin
    raise ValueError("cria_posicao: argumentos invalidos")


def cria_copia_posicao(posi):  #construtor
    """
    :argumento posi: posicao
    :return: posicao
    Esta funcao recebe uma posicao e devolve outra com um id() diferente
    Exemplos:
    >>> posicao == cria_copia_posicao(posicao)
    True
    >>> posicao is cria_copia_posicao(posicao) 
    False
    """
    return "".join(posi)


def obter_pos_c(posi):  #seletor
    """
    :argumento posi: posicao
    :return: str 
    Esta funcao recebe uma posicao, e retorna a sua coluna
    >>> obter_pos_l(cria_posicao('a','1'))
    'a'
    """
    return posi[0]


def obter_pos_l(posi):  #seletor
    """
    :argumento posi: posicao
    :return: linha da posicao
    Esta funcao recebe uma posicao, e retorna a sua linha
    >>> obter_pos_l(cria_posicao('a','1'))
    '1'
    """
    return posi[1]


def eh_posicao(posi):  #reconhecedor
    """
    :argumento posi: universal
    :return: booleano
    Esta funcao devolve um valor booleano tendo em conta se a posicao e uma 
    posicao valida.
    exemplos:
    >>> eh_posicao(cria_posicao('a','1'))
    True
    >>> eh_posicao(cria_posicao('d','1'))
    False
    """
    todasPosi = [c + l for l in ("1", "2", "3") for c in ("a", "b", "c")]
    return posi in todasPosi


def posicoes_iguais(posi1, posi2):  #teste
    """
    :argumento posi1: posicao
    :argumento posi2: posicao
    :return: booleano
    Esta funcao recebe duas posicoes e retorna uma valor booleano tendo 
    em conta se os argumentos sao posicoes, e se sao iguais
    exemplos:
    >>> posicoes_iguais(cria_posicao('b', '3'),cria_posicao('a', '2'))
    False
    """
    if eh_posicao(posi1) and eh_posicao(posi2):
        return (obter_pos_l(posi1) == obter_pos_l(posi2)
                and obter_pos_c(posi1) == obter_pos_c(posi2))
    return False


def posicao_para_str(posi):  #transformador
    """
    :argumento posi: posicao
    :return: str
    Esta funcao recebe uma posicao e retorna uma cadeia de caracteres com a 
    coluna e com a linha ('ColunaLinha')
    exemplos:
    >>> posicao_para_str(criar_posicao('a','1'))
    'a1'
    """
    return posi


def obter_posicoes_adjacentes(posi):  #Alto nivel
    """
    :argumento posi: posicao
    :return: tuplo de posicoes
    Esta funcao recebe uma posicao e devolve 
    todas as suas pecas adjacentes em tuplo.
    Esta funcao, sendo de alto nivel, respeita a barreira da abstracao
    exemplos:
    >>> p2 = cria_posicao('b', '3')
    >>> tuple(posicao_para_str(p) for p in obter_posicoes_adjacentes(p2))
    ('b2', 'a3', 'c3')
    """
    posiAdj = {
        'a1': ('b1', 'a2', 'b2'),
        'b1': ('a1', 'c1', 'b2'),
        'c1': ('b1', 'b2', 'c2'),
        'a2': ('a1', 'b2', 'a3'),
        'b2': ('a1', 'b1', 'c1', 'a2', 'c2', 'a3', 'b3', 'c3'),
        'c2': ('c1', 'b2', 'c3'),
        'a3': ('a2', 'b2', 'b3'),
        'b3': ('b2', 'a3', 'c3'),
        'c3': ('b2', 'c2', 'b3')
    }
    y = ()
    for p in posiAdj[posicao_para_str(posi)]:
        y = y + (cria_posicao(p[0], p[1]), )
    return y


# ------------------------------TAD-Peca---------------------------------------#
#Neste caso, a interpretacao interna escolhida foi ('[X]'[O]'[ ]') pois
#torna-se mais facil de entender o seu funcionamento, e facilita o decorrer
#do projeto.
#
#interpretacao interna -> ('[X]'[O]'[ ]')
#
#cria_peca:str -> peca
#cria_copia_peca:peca -> peca
#eh_peca:universal -> booleano
#pecas_iguais:peca x peca -> booleano
#peca_para_str:peca -> str
#peca_para_inteiro:peca -> inteiro
# -----------------------------------------------------------------------------#
def cria_peca(peca_str):  #construtor
    """
    :argumento peca_str: str
    :return: peca
    Esta funcao recebe uma cadeia de caracteres ('X','O',' ') e retorna
    a interpretacao interna da penca.
    Se os argumentos nao forem validos, a funcao retorna com um ValueError
    """
    pote = {"X": "[X]", "O": "[O]", " ": "[ ]"}
    if type(peca_str) == str and peca_str in ["X", "O", " "]:
        return pote[peca_str]
    raise ValueError("cria_peca: argumento invalido")


def cria_copia_peca(peca):  #construtor
    """
    :argumento peca: peca
    :return: peca
    Esta funcao recebe uma peca e devolve outra com um id() diferente
    Exemplos:
    >>> peca = cria_peca(peca_str)
    >>> peca == cria_copia_peca(peca)
    True
    >>> peca is cria_copia_peca() 
    False
    """
    return "".join(peca)


def eh_peca(peca):  #reconhecedor
    """
    :argumento peca: universal
    :return: booleano
    Esta funcao devolve um valor booleano dependendo se o argumento for um
    TAD peca
    """
    return type(peca) == str and peca in ["[X]", "[O]", "[ ]"]


def pecas_iguais(peca1, peca2):  #Teste
    """
    :argumento peca1: peca
    :argumento peca2: peca
    :return: booleano
    Esta funcao devolve um valor booleano dependendo se os agumentos: peca1 e 
    peca 2 forem iguais e TAD pecas.
    >>> pecas_iguais(cria_peca('X'),cria_peca('X'))
    True
    >>> pecas_iguais(cria_peca('X'),cria_peca('O'))
    False
    """
    if eh_peca(peca1) and eh_peca(peca2):
        return peca1 == peca2
    return False


def peca_para_str(peca):  #transformador
    """
    :argumento peca: peca
    :return: str
    Esta funcao recebe um TAD peca e devolve uma cadeia de caracteres que 
    representa a sua respetiva peca ('[X]','[O]','[ ]')
    Exemplos:
    >>> peca_para_str(criar_peca('X'))
    '[X]'
    """
    return peca


def peca_para_inteiro(peca):  # Alto nivel
    """
    :argumento peca: peca
    :return: inteiro
    Esta funcao recebe como argumento um TAD peca e devolve 1, -1 , 0 
    dependendo, respetivamente se a peca for do jogador 'X','O' ou ' '(livre)
    Exemplos:
    >>> peca_para_inteiro(criar_peca('X'))
    1
    """
    strPeca = peca_para_str(peca)
    pote = {"[X]": 1, "[O]": -1, "[ ]": 0}
    return pote[strPeca]


# -------------------------------TAD-Tabuleiro---------------------------------#
#Esta escolha foi assim feita pois, sendo um conjunto de listas, esta mesma
#e mutavel podendo assim ser modificada destrutivamente como e pedido em
#certas funcoes. Para alem disso, cada conjunto de listas (com um total de 3)
#representa uma linha no tabuleiro, sendo assim mais facil de visualizar.
#
#interpretacao interna = [[[],[],[]],[[],[],[]],[[],[],[]]]
#
#cria_tabuleiro:{} ->tabuleiro
#cria_copia_tabuleiro:tabuleiro ->tabuleiro
#str_para_int:string -> int
#posi_to_coord:int -> coodenadas
#obter_peca:tabuleiroxposicao ->peca
#obter_vetor:tabuleiroxstr ->tuplo de pecas
#coloca_peca:tabuleiroxpecaxposicao ->tabuleiro
#remove_peca:tabuleiroxposicao ->tabuleiro
#move_peca:tabuleiroxposicaoxposicao ->tabuleiro
#eh_terminado:tabuleiro ->list
#eh_tabuleiro:universal ->booleano
#eh_posicao_livre:tabuleiroxposicao ->booleano
#tabuleiros_iguais:tabuleiroxtabuleiro ->booleano
#tabuleiro_para_str:tabuleiro ->str
#tuplo_para_tabuleiro:tuplo ->tabuleiro
#obter_ganhador:tabuleiro ->peca
#obter_posicoes_livres:tabuleiro ->tuplo de posicoes
#obter_posicoes_jogador:tabuleiroxpeca ->tuplo de posicoes
# -----------------------------------------------------------------------------#


def cria_tabuleiro():  #construtor
    """
    :argumento {}: TypeNull
    :return: TAD tabuleiro
    Esta funcao cria um TAD tabuleiro vazio
    """
    tabDefault = [cria_peca(" ") for x in range(9)]
    rangeOfTab = range((len(tabDefault) + 3 - 1) // 3)
    return [tabDefault[i * 3:(i + 1) * 3] for i in rangeOfTab]


def cria_copia_tabuleiro(tab):  #construtor
    """
    :argumento tab: tabuleiro
    :return: tabuleiro
    Esta funcao recebe um TAD tabuleiro e devolve um TAD tabuleiro com um id()
    diferente
    Exemplos:
    >>> tabuleiro = cria_tabuleiro()
    >>> tabuleiro == cria_copia_tabuleiro(tabuleiro)
    True
    >>> peca is cria_copia_tabuleiro(tabuleiro) 
    False
    """
    pote = []
    for j in tab:
        for h in j:
            pote = pote + [h]
    return [pote[i * 3:(i + 1) * 3] for i in range((len(pote) + 3 - 1) // 3)]


def str_para_int(posi_str):  #modificador
    """
    :argumento posi_str: string
    :return: inteiro
    Esta funcao recebe uma cadeia de caracteres e 
    devolve um inteiro representado o seu valor em inteiro
    Exemplos:
    >>> str_para_int('a1')
    1
    >>> str_para_int('c3')
    9
    """
    x = [posi_str[i:i + 1] for i in range(0, len(posi_str), 1)]
    dicPote = {
        "a": ["1", "4", "7"],
        "b": ["2", "5", "8"],
        "c": ["3", "6", "9"]
    }
    return int(dicPote[x[0]][int(x[1]) - 1])


def posi_to_coord(posi_int):  #modificador
    """
    :argumento posi_int: posicao inteiro
    :return: coordenadas
    Esta funcao recebe uma posicao de 0 a 9 representando, repetivamente 'a1' e
    'c3' e devolve um tuplo com as suas coordenadas no tabuleiro
    """
    return (posi_int - 1) // 3, (posi_int - 1) % 3


def obter_peca(tab, posi):  #seletor
    """
    :argumento tab: tabuleiro
    :argumento posi: posicao
    :return: peca
    Esta funcao recebe como argumento um tabuleiro e uma posicao e, devolve a 
    peca correspondente
    Exemplos:
    >>> t = cria_tabuleiro()
    >>> obter_peca(t,'a1')
    '[ ]'
    """
    posi = str_para_int(posicao_para_str(posi))
    return tab[posi_to_coord(posi)[0]][posi_to_coord(posi)[1]]


def obter_vetor(tab, LinCol):  #seletor
    """
    :argumento tab: tabuleiro 
    :argumento LinCol: str
    :return: tuplo
    Esta funcao recebe um tabuleiro e uma cadeia de caracteres.
    Essa mesma cadeia pode representar uma linha ('1','2','3')
    ou uma coluna ('a','b','c'). A mesma retorna um vetor com as pecas
    dessa mesma coluna/linha
    Exemplos:
    >>> t = tuplo_para_tabuleiro(((0,1,-1),(-0,1,-1),(1,0,-1)))
    >>> tuple(peca_para_str(peca) for peca in obter_vetor(t, 'a'))
    ('[ ]', '[ ]', '[X]')
    """
    dicPoteCol = {"a": 1, "b": 2, "c": 3}
    if LinCol in ["1", "2", "3"]:  # linha
        return tuple(tab[int(LinCol) - 1])
    else:  # coluna
        return tuple((
            tab[0][int(dicPoteCol[LinCol]) - 1],
            tab[1][int(dicPoteCol[LinCol]) - 1],
            tab[2][int(dicPoteCol[LinCol]) - 1],
        ))


def coloca_peca(tab, peca, posi):  #modificador
    """
    :argumento tab: tabuleiro
    :argumento peca: peca
    :argumento posi: posicao
    :return: tabuleiro
    Esta funcao recebe um tabuleiro e coloca a peca na posicao enunciada.
    A mesma retorna um tabuleiro com a peca colocada. Esta colocacao e feita de
    forma destrutiva
    Exemplos:
    >>> t = cria_tabuleiro()
    >>> tabuleiro_para_str(coloca_peca(t, cria_peca('X'),cria_posicao('a','1')))
    '   a   b   c\n1 [X]-[ ]-[ ]\n   | \\ | / |\n
    2 [ ]-[ ]-[ ]\n   | / | \\ |\n3 [ ]-[ ]-[ ]'
    """
    posi = str_para_int(posicao_para_str(posi))
    for x in range(0, 10):
        if x == posi:
            tab[posi_to_coord(posi)[0]][posi_to_coord(posi)[1]] = peca
    return tab


def remove_peca(tab, posi):  #modificador
    """
    :argumento tab: tabuleiro
    :argumento posi: posicao
    :return: tabuleiro
    Esta funcao recebe um tabuleiro e remove a peca na posicao enunciada.
    A mesma retorna um tabuleiro com a peca removida. Esta remocao e feita de
    forma destrutiva
    Exemplos:
    >>> t = tuplo_para_tabuleiro(((1,0,0),(0,0,0),(0,0,0)))
    >>> tabuleiro_para_str(remove_peca(t,cria_posicao('a','1')))
    '   a   b   c\n1 [ ]-[ ]-[ ]\n   | \\ | / |\n
    2 [ ]-[ ]-[ ]\n   | / | \\ |\n3 [ ]-[ ]-[ ]'
    """
    return coloca_peca(tab, cria_peca(" "), posi)


def move_peca(tab, posi1, posi2):  #modificador
    """
    :argumento tab: tabuleiro
    :argumento posi1: posicao
    :argumento posi2: posicao
    Esta funcao recebe um tabuleiro e move a peca presente na primeira posicao
    fornecida para a segunda.
    A mesma retorna um tabuleiro com a peca movida. Esta mudanca e feita de
    forma destrutiva
    >>> t = tuplo_para_tabuleiro(((1,0,0),(0,0,0),(0,0,0)))
    >>> tabuleiro_para_str(move_peca(t, 
    cria_posicao('a','1'),cria_posicao('b','1')))
    '   a   b   c\n1 [ ]-[X]-[ ]\n   | \\ | / |\n
    2 [ ]-[ ]-[ ]\n   | / | \\ |\n3 [ ]-[ ]-[ ]'
    """
    peca = obter_peca(tab, posi1)
    tab = remove_peca(tab, posi1)
    tab = coloca_peca(tab, peca, posi2)
    return tab


def eh_terminado(tab):  #reconhecedor
    """
    :argumento tab: tabuleiro
    :return: lista
    Esta funcao analiza o tabuleiro e retorna a peca com o vencedor/vencedores
    em forma de lista, ou seja, se algum jogador possuir um 3 em linha, a peca
    desse mesmo jogador sera colocada numa lista.
    Exemplos:
    >>> t = tuplo_para_tabuleiro(((0,1,-1),(-0,1,-1),(1,0,-1)))
    >>> peca_para_str(eh_terminado(t))
    ['[O]']
    """
    dicpote = {1: "a", 2: "b", 3: "c"}
    ganhadores = []
    for potePeca in [cria_peca("X"), cria_peca("O")]:
        potel = []
        potec = []
        for i in range(1, 4):
            potel = potel + list(obter_vetor(tab, str(i)))
            potec = potec + list(obter_vetor(tab, dicpote[i]))
            if all((pecas_iguais(potel[x], potePeca)) for x in range(0, 3)):
                ganhadores = ganhadores + [potel[0]]
            elif all((pecas_iguais(potec[x], potePeca)) for x in range(0, 3)):
                ganhadores = ganhadores + [potec[0]]
            potel = []
            potec = []
    return ganhadores


def eh_tabuleiro(tab):  #reconhecedor
    """
    :argumento tab: universal
    :return: boolean
    Esta funcao avalia se um tabuleiro e valido. O metedo utilizado nesta mesma
    foi de uma forma de contagem. Foi criado 2 contadores que garantiam que 
    cada jogador nao possuia mais que 3 pecas, que cada jogador possuia igual
    ou mais(ou menos) 1 que o adversario, e que apenas existe apenas 1 vencedor.
    Retorna entao um valor boolean se estes criterios forem respeitados.
    Exemplos:
    >>> t = tuplo_para_tabuleiro(((0,1,-1),(-0,1,-1),(1,0,-1)))
    >>> eh_tabuleiro(t)
    True
    """
    counter1 = 0
    counter2 = 0
    if type(tab) != list:
        return False
    if len(tab) != 3:
        return False
    for j in range(0, 3):
        for i in range(0, 3):
            if type(tab[j]) != list:
                return False
            if pecas_iguais(tab[j][i], cria_peca("X")):
                counter1 += 1
            if pecas_iguais(tab[j][i], cria_peca("O")):
                counter2 += 1
    return ((counter1 + 1 == counter2 or counter1 - 1 == counter2
             or counter1 == counter2) and counter1 <= 3
            and isinstance(tab, list) and len(tab) == 3
            and (len(eh_terminado(tab)) == 0 or len(eh_terminado(tab)) == 1))


def eh_posicao_livre(tab, posi):  #reconhecedor
    """
    :argumento tab: tabuleiro
    :argumento posi: posicao
    :return: boolean
    Esta funcao recebe um tabuleiro e uma posicao nesse mesmo tabuleiro e
    retorna True se essa mesma posicao nao estiver ocupada
    Exemplos:
    >>> t = tuplo_para_tabuleiro(((0,1,-1),(-0,1,-1),(1,0,-1)))
    >>> eh_posicao_livre(t,cria_posicao('a','1'))
    True
    """
    return pecas_iguais(obter_peca(tab, posi), cria_peca(" "))


def tabuleiros_iguais(tab1, tab2):  #teste
    """
    :argumento tab1: tabuleiro
    :argumento tab2: tabuleiro
    :return: boolean
    Esta funcao recebe dois tabuleiros e retorna se estes mesmos sao iguais.
    Para isso, e verificado peca a peca de cada tabuleiro a sua igualdade.
    Exemplos:
    >>> t1 = tuplo_para_tabuleiro(((0,1,-1),(-0,1,-1),(1,0,-1)))
    >>> t2 = tuplo_para_tabuleiro(((0,1,-1),(-0,1,-1),(1,0,1)))
    >>> tabuleiros_iguais(t1,t2)
    False
    """
    if eh_tabuleiro(tab1) and eh_tabuleiro(tab2):
        return all(
            pecas_iguais(tab1[h][j], tab2[h][j]) for j in (0, 1, 2)
            for h in (0, 1, 2))
    return False


def tabuleiro_para_str(tab):  #transformador
    """
    :argumento tab: tabuleiro
    :return: str
    Esta funcao recebe um tabuleiro e retorna com uma cadeia de caracteres.
    E utilizada uma string que acomula todas as pecas de cada posicoes e, com um
    simples .format(), consegue-se representar este tabuleiro numa string.
    Exemplos:
    >>> t = tuplo_para_tabuleiro(((0,1,-1),(-0,1,-1),(1,0,-1)))
    >>> tabuleiro_para_str(t)
    '   a   b   c\n1 [ ]-[X]-[O]\n   | \\ | / |\n
    2 [ ]-[X]-[O]\n   | / | \\ |\n3 [X]-[ ]-[O]'
    """
    pote = ""
    for c in (0, 1, 2):
        for l in (0, 1, 2):
            for pecas in ("X", "O", " "):
                if pecas_iguais(tab[c][l], cria_peca(pecas)):
                    pote = pote + pecas
    return "   a   b   c\n1 [{}]-[{}]-[{}]\n   | \\ | / |\n2 [{}]-[{}]-[{}]\n\
   | / | \\ |\n3 [{}]-[{}]-[{}]".format(*pote)


def tuplo_para_tabuleiro(tup):  #transformador
    """
    :argumento tup: tuplo
    :return: tabuleiro
    Esta funcao recebe um tuplo na forma ((0,0,0),(0,0,0),(0,0,0)) e onde:
    1 = cria_peca('X')
    -1 = cria_peca('O')
    0 = cria_peca(' ')
    e transforma esse tuplo num tabuleiro.
    """
    dicNC = {1: cria_peca("X"), -1: cria_peca("O"), 0: cria_peca(" ")}
    poteTab = [dicNC[tup[l][c]] for l in (0, 1, 2) for c in (0, 1, 2)]
    return [
        [poteTab[x] for x in range(0, 3)],
        [poteTab[x] for x in range(3, 6)],
        [poteTab[x] for x in range(6, 9)],
    ]


def obter_ganhador(tab):  #Alto nivel
    """
    :argumento tab: tabuleiro
    :return: peca
    Esta funcao recebe um tabuleiro e retorna a peca que corresponde ao jogador
    vencedor desse mesmo tabuleiro, ou seja, o mesmo que tiver um 3 em linha. 
    Exemplos:
    >>> t = tuplo_para_tabuleiro(((0,1,-1),(-0,1,-1),(1,0,-1)))
    >>> peca_para_str(obter_ganhador(t))
    '[O]'
    """
    return eh_terminado(tab)[0] if eh_terminado(tab) != [] else cria_peca(" ")


def obter_posicoes_livres(tab):  #Alto nivel
    """
    :argumento tab: tabuleiro
    :return: tuplo de posicoes
    Esta funcao recebe um tabuleiro e retorna um tuplo com todas as suas
    posicoes livres. E utilizado o map e list para filtrar uma lista constituida
    por todas as posicoes do tabuleiro e, verificando se essas posicoes estao
    livres, formam uma lista que e transformada e retornada em forma de tuplo
    Exemplos:
    >>> t = tuplo_para_tabuleiro(((0,1,-1),(-0,1,-1),(1,0,-1)))
    >>> tuple(posicao_para_str(p) for p in obter_posicoes_livres(t))
    ('a1', 'a2', 'b3')
    """
    todasPosi = [
        cria_posicao(c, l) for l in ("1", "2", "3") for c in ("a", "b", "c")
    ]
    verPosiLiv = list(
        map(
            lambda x: x,
            filter(
                lambda x: eh_posicao_livre(tab, x),
                todasPosi,
            ),
        ))
    return tuple(verPosiLiv)


def obter_posicoes_jogador(tab, peca):  #Alto nivel
    """
    :argumento tab: tabuleiro
    :argumento peca: peca
    :return: tuplo de posicoes
    Esta funcao recebe um tabuleiro e uma peca e, retorna um tuplo com todas as
    posicoes do tabuleiro que possuem essa mesma peca.
    E utilizado o map e list para filtrar uma lista constituida
    por todas as posicoes do tabuleiro e, verificando se essas posicoes possuem
    a peca igual a introduzida, formam uma lista que e transformada
    e retornada em forma de tuplo
    Exemplos:
    >>> t = tuplo_para_tabuleiro(((0,1,-1),(-0,1,-1),(1,0,-1)))
    >>> peca = cria_peca('X')
    >>> tuple(posicao_para_str(p) for p in obter_posicoes_jogador(t,peca))
    ('b1', 'b2', 'a3')
    """
    todasPosi = [
        cria_posicao(c, l) for l in ("1", "2", "3") for c in ("a", "b", "c")
    ]
    verPosiOcup = list(
        map(
            lambda x: x,
            filter(
                lambda x: not any(
                    posicoes_iguais(x, h) for h in obter_posicoes_livres(tab))
                and pecas_iguais(obter_peca(tab, x), peca),
                todasPosi,
            ),
        ))
    return tuple(verPosiOcup)


# ------------------------Funcoes-Adicionais-(2.2)-----------------------
def contrar_peca(peca):  # AUX
    """
    :argumento peca: peca
    :return: peca
    Esta funcao recebe uma peca e devolve o seu contrario (x -> O, O -> X)
    Exemplos:
    >>> contrar_peca(cria_peca('X'))
    '[O]'
    """
    if pecas_iguais(peca, cria_peca("X")):
        return cria_peca("O")
    elif pecas_iguais(peca, cria_peca("O")):
        return cria_peca("X")


def possivel_mover(tab, peca):
    """
    :argumento tab: tabuleiro
    :argumento peca: peca
    :return: boolean
    Esta funcao recebe um tabuleiro e uma peca e verifica se todas as pecas
    desse mesmo tipo estao presas, devolvendo um valor boolean de True se
    existir pelo menos um movimento possivel.
    """
    # AUX (maybe podemos colocar esta dentro do obter_movimento_manual)
    return any([
        any(g) for g in ([(
            [eh_posicao_livre(tab, i) for i in obter_posicoes_adjacentes(j)])
                          for j in obter_posicoes_jogador(tab, peca)])
    ])


def eh_posicao_str(posi_str):  #reconhecedor
    """
    :argumento posi_str: 
    :return: boolean
    Esta funcao devolve um valor booleano tendo em conta se a posicao e uma 
    posicao valida.
    exemplos:
    >>> eh_posicao_str('a1'))
    True
    >>> eh_posicao_str('d1'))
    False
    """
    todasPosi = [c + l for l in ("1", "2", "3") for c in ("a", "b", "c")]
    return len(posi_str) == 2 and posi_str in todasPosi


def obter_movimento_manual(tab, peca):
    """
    :argumento tab: tabuleiro
    :argumento peca: peca
    :return: tuplo de posicoes
    Esta funcao recebe um tabuleiro e uma peca. A mesma verifica a fase do jogo
    (colocacao ou movimento) e recebe como input do utilizador, um movimento 
    ou uma colocacao. Se for uma colocacao, e verificado se a posicao e uma
    posicao livre. Se for um movimento, e verificado se:
    -a peca esta presa entao o jogador pode jogar um movimento semelhante a a1a1
    -no movimento e na colocacao, a peca esta a ir 
    para uma casa livre e adjacente
    -a peca que se quer retirar no movimento e do jogador
    -a colocar a peca, a posicao e uma casa livre
    Se estes criterios nao forem respeitados, esta funcao levanta um ValueError
    """
    if len(obter_posicoes_jogador(tab, peca)) == 3:
        jogada = str(input("Turno do jogador. Escolha um movimento: "))
    else:
        jogada = str(input("Turno do jogador. Escolha uma posicao: "))
    poteJogada = [jogada[i:i + 1] for i in range(0, len(jogada), 1)]
    #separa a str com a jogada ('a1' -> ['a','1'])
    if len(poteJogada) == 2:  #uma colocacao
        if eh_posicao_str(jogada):
            posicao = cria_posicao(jogada[0], jogada[1])
            if (any(
                    posicoes_iguais(posicao, p)
                    for p in obter_posicoes_livres(tab))
                    and len(obter_posicoes_jogador(tab, peca)) != 3):
                return (posicao, )
        raise ValueError("obter_movimento_manual: escolha invalida")
    elif len(poteJogada) == 4:  #um movimento
        jogadaRetirar = poteJogada[0] + poteJogada[1]
        jogadaColocar = poteJogada[2] + poteJogada[3]
        if eh_posicao_str(jogadaRetirar) and eh_posicao_str(jogadaColocar):
            jogadaRetirar = cria_posicao(jogadaRetirar[0], jogadaRetirar[1])
            jogadaColocar = cria_posicao(jogadaColocar[0], jogadaColocar[1])
            if (not possivel_mover(tab, peca)
                    and posicoes_iguais(jogadaColocar, jogadaRetirar) and any(
                        posicoes_iguais(jogadaColocar, p)
                        for p in obter_posicoes_jogador(tab, peca))):
                return (jogadaColocar, jogadaColocar)
            elif (not any(
                    posicoes_iguais(jogadaRetirar, p)
                    for p in obter_posicoes_jogador(tab, peca)) or any(
                        posicoes_iguais(jogadaRetirar, p)
                        for p in obter_posicoes_livres(tab)) or not any(
                            posicoes_iguais(jogadaColocar, p)
                            for p in obter_posicoes_livres(tab))
                  or not any(
                      posicoes_iguais(jogadaColocar, p)
                      for p in obter_posicoes_adjacentes(jogadaRetirar))
                  ) or len(obter_posicoes_jogador(tab, peca)) != 3:
                raise ValueError("obter_movimento_manual: escolha invalida")
            else:
                return (jogadaRetirar, jogadaColocar)
    raise ValueError("obter_movimento_manual: escolha invalida")


def eh_colocacao(tab, peca):
    """
    :argumneto tab: tabuleiro
    :argumento peca: peca
    :return: boolean
    Esta funcao verifica se a fase do jogo, colocacao ou movimento.
    """
    return len(obter_posicoes_jogador(tab, peca)) < 3


def concluir_jogo(tab, peca):  # vitoria
    """
    :argumento tab: tabuleiro
    :argumento peca: peca
    :return: posicao
    Esta funcao devolve uma posicao se for possivel terminar o jogo na proxima
    jogada.
    """
    if len(obter_posicoes_jogador(tab, peca)) >= 2:
        pote = []
        for x in obter_posicoes_livres(tab):
            poteTab = cria_copia_tabuleiro(tab)
            if pecas_iguais(obter_ganhador(coloca_peca(poteTab, peca, x)),
                            peca):
                pote = pote + [x]
        if pote:
            return pote


def bloqueio_vitoria(tab, peca):  # bloqueio da vitoria
    """
    :argumento tab: tabuleiro
    :argumento peca: peca
    :return: posicao
    Esta funcao devolve a posicao que possiblitava a vitoria para o jogador
    contrario na proxima jogada
    """
    if len(obter_posicoes_jogador(tab, contrar_peca(peca))) >= 2:
        return concluir_jogo(tab, contrar_peca(peca))


def jogar_centro(tab, peca):  # jogar na posicao central
    """
    :argumento tab: tabuleiro
    :argumento peca: peca
    :return: posicao
    Esta funcao devolve a posicao central (b2) se esta mesma estiver livre
    """
    for j in obter_posicoes_livres(tab):
        if posicoes_iguais(cria_posicao("b", "2"), j):
            return [cria_posicao("b", "2")]


def jogar_cantos(tab, peca):  # jogar num dos cantos por ordem
    """
    :argumento tab: tabuleiro
    :argumento peca: peca
    :return: posicao
    Esta funcao devolve a primeira posicao dos cantos (a1,c1,a3,b3)
    que estiver livre
    """
    pote = list(x for x in [
        cria_posicao('a', '1'),
        cria_posicao('c', '1'),
        cria_posicao('a', '3'),
        cria_posicao('c', '3')
    ] if any(posicoes_iguais(x, j) for j in obter_posicoes_livres(tab)))
    return pote


def jogar_lateral(tab, peca):  # jogar numa lateral
    """
    :argumento tab: tabuleiro
    :argumento peca: peca
    :return: posicao
    Esta funcao devolve a primeira posicao lateral (b1,a2,c2,b3)
    que estiver livre 
    """
    pote = list(x for x in [
        cria_posicao('b', '1'),
        cria_posicao('a', '2'),
        cria_posicao('c', '2'),
        cria_posicao('b', '3')
    ] if any(posicoes_iguais(x, j) for j in obter_posicoes_livres(tab)))
    return pote


def minimax(tab, peca, profundidade, seq_movimentos):
    """
    :argumento tab: tabuleiro
    :argumento peca: peca
    :argumento profundidade: int
    :argumento seq_movimentos: list
    :return: posicao
    Esta funcao recursiva e um algoritmo que, verifica todas as
    jogadas possiveis,dependendo de uma profundidade de busca introduzida,
    e verifica qual e o melhor resultado possivel para minimizar a derrota.
    Este algoritmo retorna um valor de tabuleiro, que depende do vencedor, e 
    uma sequencia de movimentos que o mesmo foi procurando.
    Se a peca do jogador for X, o objetivo e maximizar o valor do tabuleiro e
    minimizar se for O. 
    """
    if not pecas_iguais(obter_ganhador(tab),
                        cria_peca(" ")) or profundidade == 0:
        #existe um vencedor ou a profundidade chegou a 0
        valor_tabuleiro = peca_para_inteiro(obter_ganhador(tab))
        return valor_tabuleiro, seq_movimentos
    else:
        melhor_resultado = peca_para_inteiro(contrar_peca(peca))
        melhor_seq_movimentos = []
        for i in obter_posicoes_jogador(tab, peca):
            for j in obter_posicoes_adjacentes(i):
                #para cada movimento possivel:
                if eh_posicao_livre(tab, j):
                    Copytab = cria_copia_tabuleiro(tab)
                    move_peca(Copytab, i, j)
                    novo_movimento = [i, j]
                    novo_resultado, nova_seq_movimentos = minimax(
                        Copytab,
                        contrar_peca(peca),
                        profundidade - 1,
                        seq_movimentos + novo_movimento,
                    )
                    #aqui e verificado se a melhor sequencia ainda nao foi
                    #definida e, dependendo da peca, verificar se o
                    #novo resultado(1,0,-1) e melhor ou pior
                    # que o melhor resultado anterior
                    if ((melhor_seq_movimentos == [])
                            or (pecas_iguais(peca, cria_peca('X'))
                                and novo_resultado > melhor_resultado)
                            or (pecas_iguais(peca, cria_peca('O'))
                                and novo_resultado < melhor_resultado)):
                        melhor_resultado = novo_resultado
                        melhor_seq_movimentos = nova_seq_movimentos
        return melhor_resultado, melhor_seq_movimentos


def obter_movimento_auto(tab, peca, dific):
    """
    :argumento tab: tabuleiro
    :argumento peca: peca
    :argumento dific: cadeia de caracteres
    Esta funcao recebe um tabuleiro, uma peca e uma dificuldade em string.
    Na fase de colocacao, esta funcao utiliza as funcoes previamente enunciadas.
    Na fase de movimento:
    - facil: mover a primeira peca do jogador para a primeira posicao possivel
    -normal: utiliza o minimax com uma profundidade de 1
    -dificil: utiliza o monimax com uma profundidade de 5
    """
    if eh_colocacao(tab, peca):  # fase de colocacao
        for jogada in [
                concluir_jogo,
                bloqueio_vitoria,
                jogar_centro,
                jogar_cantos,
                jogar_lateral,
        ]:
            if jogada(tab, peca) and any(
                    posicoes_iguais(jogada(tab, peca)[0], h)
                    for h in obter_posicoes_livres(tab)):
                return (jogada(tab, peca)[0], )

    else:  # fase de movimento
        if dific == "facil":
            for i in obter_posicoes_jogador(tab, peca):
                for x in obter_posicoes_livres(tab):
                    for h in obter_posicoes_adjacentes(i):
                        if posicoes_iguais(x, h):
                            return (i, x)
        if dific == "normal":
            return tuple(minimax(tab, peca, 1, [])[1][:2])
        if dific == 'dificil':
            return tuple(minimax(tab, peca, 5, [])[1][:2])


def moinho(peca_str, dific):
    """
    :argumento peca_str: str
    :argumento dific: str
    Esta funcao recebe duas cadeias de caracteres, uma sendo a peca do jogador
    e a outra a dificuldade. Esta funcao e a funcao final, que torna o jogo
    completamente operacional. Neste jogo, o jogador que joga primeiro e sempre
    a peca 'X'. A mesma devolve, quando o jogo for terminado, ['X'] ou ['O'],
    dependendo do vencedor do jogo. 
    """
    print(
        'Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {}.'.format(dific))
    tab = cria_tabuleiro()
    print(tabuleiro_para_str(tab))
    if peca_str == '[X]':
        count = 0
        peca = cria_peca('X')
    else:
        count = 1
        peca = cria_peca('O')
    while pecas_iguais(obter_ganhador(tab), cria_peca(' ')):
        if count % 2 == 0:
            jogadaHumano = obter_movimento_manual(tab, peca)
            if len(jogadaHumano) == 1:
                coloca_peca(tab, peca, jogadaHumano[0])
            else:
                if not posicoes_iguais(jogadaHumano[0], jogadaHumano[1]):
                    move_peca(tab, jogadaHumano[0], jogadaHumano[1])
            print(tabuleiro_para_str(tab))
            count += 1
        elif count % 2 != 0:
            jogadaAI = obter_movimento_auto(tab, contrar_peca(peca), dific)
            print('Turno do computador ({}):'.format(dific))
            if len(jogadaAI) == 1:
                coloca_peca(tab, (contrar_peca(peca)), jogadaAI[0])
            else:
                if not posicoes_iguais(jogadaAI[0], jogadaAI[1]):
                    move_peca(tab, jogadaAI[0], jogadaAI[1])
            print(tabuleiro_para_str(tab))
            count += 1
    return peca_para_str(obter_ganhador(tab))