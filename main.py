from audioop import reverse
from curses.ascii import FF
from sqlalchemy import true


def main():
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # questao 1:
    matriz = open("./A.txt", "r")
    A = list()
    B = list()
    arestasMultiplas = list()
    lacos = list()

    for line in matriz:
        for i in line.split():
            B.append(i)

    i = list(map(int, B))
    matriz.close()

    print('-='*30)
    print('\nQuestão 1:')

    for item in i:
        if item > 1:
            check = True;
        else:
            check = False;
    
    if check == True:
        print('\nÉ um grafo simples, pois não ele possui adjacências multiplas ou laços.\n');
    else:
        print('\nNão é um grafo simples, pois ele possui adjacências multiplas ou laços.\n');

    # adiciona e converte em lista na matriz A
    matriz = open("./A.txt", "r")
    for line in matriz:
        A.append(list(map(int, line.split())))
    matriz.close()

    # imprime quais são os locais de adjacências multiplas
    aux = 0  # auxiliar para verificar se é um local de adjacências multiplas
    if check == False:
        for line in A:
            for col in range(len(A)):
                # checka se o elemento tem arestas multiplas ou é um laco e adiciona em uma matriz que indica quais são os locais de adjacências multiplas ou lacos
                if line[col] > 1:
                    arestasMultiplas.append([(aux + 1), (col + 1)])
                elif line[col] >= 1 and (col == aux):
                    lacos.append((col))
            aux = aux + 1

        # colocando as colunas em ordem crescente
        arestasMultiplas.sort()
        lacos.sort()
        # imprimindo de fato:
        for item in arestasMultiplas:
            print('\nO(s) local(s) de adjacências multiplas é: ', item, end=', ')
        print('\n')
        for item in lacos:
            print('\nO(s) local(s) de laços é: %d %d [lin][col]' % (
                (item + 1), (item + 1)), end=', ')
        print('\n')
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    # questao 2
    print('-='*30)
    print('\nQuestão 2:')
    existeOGrafo, graus, soma = seqGrausESoma(A)

    if not existeOGrafo:
        print('O grafo não existe!\n')
        return

    # questao 3
    print('-='*30)
    print('\nQuestão 3:')

    print("O número de arestas é: %d" % (soma/2))

    # questao 4
    print('-='*30)
    print('\nQuestão 4:')

    if grafoCompleto(A, check):
        print("Sim, pois é um grafo simples em que todo vértice é adjacente a todos os outros vértices. ")
    else:
        print("Não, pois não é um grafo simples em que todo vértice é adjacente a todos os outros vértices. ")

    # questao 5
    print('-='*30)
    print('\nQuestão 5:')

    if grafoRegular(graus):
        print("Sim, porque todos os vértices possuem o mesmo grau.")
    else:
        print("Nao, pois os vértices não possuem o mesmo grau.")

    # questao 6
    print('-='*30)
    print('\nQuestão 6:')
    bipartido, x, y = grafoBipartido(A)
    if (bipartido):
        print("Sim, pois é um grafo cujos vértices podem ser divididos em dois conjuntos disjuntos U e V tais que toda aresta conecta um vértice em U a um vértice em V; ou seja, U e V são conjuntos\n")

        # impressão dos conjuntos U e V:
        print("\nBipartição:")
        print("X = {", end="")
        for v in x:
            if v == x[-1]:
                print("v{0}".format(v+1), end="}\n")
            else:
                print("v{0}".format(v+1), end=", ")
        
        print("Y = {", end="")
        for v in y:
            if v == y[-1]:
                print("v{0}".format(v+1), end="}\n")
            else:
                print("v{0}".format(v+1), end=", ")
    else:
        print("Não, pois não é um grafo cujos vértices podem ser divididos em dois conjuntos disjuntos U e V tais que toda aresta conecta um vértice em U a um vértice em V; ou seja, U e V são conjuntos")

    # questao 7
    print('-='*30);
    print('\nQuestão 7:');
    if (check) and (bipartido):
        print("É um grafo bipartido completo pois é um grafo simples e bipartido.");
    else:
        print("Não é um grafo bipartido completo pois não é um grafo simples ou não é um grafo bipartido.\n");
    print('-='*30);


def seqGrausESoma(Matriz):  # Verifica a sequência dos graus do Grafo
    graus = list()
    # somando todas as adjascencias de cada vértice
    for linha in range(len(Matriz)):
        graus.append(0)
        for coluna in range(len(Matriz)):
            if linha == coluna:
                graus[linha] += (int(Matriz[linha][coluna])*2)
            else:
                graus[linha] += int(Matriz[linha][coluna])

    soma = 0
    for item in range(len(graus)):
        soma += graus[item]

    if soma % 2 == 1:
        return (False, graus, soma)
    else:
        graus.sort(reverse=True)
        print("Sequência dos graus do grafo:", end=" ")
        print(*graus, sep=", ")
        return (True, graus, soma)

def grafoCompleto(matriz, check):
    if not check:
        return False
    elif check:
        for linha in range(len(matriz)):
            for coluna in range(len(matriz)):
                # Se o valor da célula for maior que 0 ela é um laço
                if (linha == coluna) and (matriz[linha][coluna] != 0):
                    return False
                # Se o valor da célula for maior que 1 ela é aresta multipla
                elif (linha != coluna) and (matriz[linha][coluna] != 1):
                    return False
    else:
        return True


def grafoRegular(graus):
    # checka se todos os elementos da matriz forem iguais
    for item in graus:
        if graus[0] == item:
            pass
        else:
            return False
    return True  # se laço for executado sem retornar falso, a funcao retorna true, já que isso significa tds elementos sao iguais


def grafoBipartido(matriz):
	x = [0]
	y = []
	check = True
	# Dar uma verificada sobre quando tiver laços
	for linha in range(len(matriz)):
		for coluna in range(len(matriz)):
			if linha in x and int(matriz[linha][coluna]) != 0 and coluna not in y:
				if coluna in x:
					check = False;
				else:
					y.append(coluna);
			elif linha in y and int(matriz[linha][coluna]) != 0 and coluna not in x:
				if coluna in y:
					check = False;
				else:
					x.append(coluna);
	if (check):
		return (True, x, y);
	else:
		return (False, False, False);


if __name__ == '__main__':
    main()
