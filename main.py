from sqlalchemy import true


def main():
    matriz = open("./A.txt", "r");
    A = list();
    B = list();
    arestasMultiplas = list();
    lacos = list();

    for line in matriz:
        for i in line.split():
            B.append(i);

    i = list(map(int, B));
    matriz.close();

    if 2 not in i:
        print('\nÉ um grafo simples, pois não ele possui adjacências multiplas ou laços.\n');
    else:
        print('\nNão é um grafo simples, pois ele possui adjacências multiplas ou laços.\n');

    # adiciona e converte em lista na matriz A
    matriz = open("./A.txt", "r");
    for line in matriz:
        A.append(list(map(int, line.split())));
    matriz.close();

    # imprime quais são os locais de adjacências multiplas
    aux = 0; # auxiliar para verificar se é um local de adjacências multiplas
    for line in A:
        for col in range(len(A)):
            # checka se o elemento tem arestas multiplas ou é um laco e adiciona em uma matriz que indica quais são os locais de adjacências multiplas ou lacos
            if line[col] > 1:
                arestasMultiplas.append([(aux + 1), (col + 1)]);
            elif line[col] >= 1 and (col == aux):
                lacos.append((col));
        aux = aux + 1;

    # colocando as colunas em ordem crescente
    arestasMultiplas.sort();
    lacos.sort();
    # imprimindo de fato:
    for item in arestasMultiplas:
            print('\nO(s) local(s) de adjacências multiplas é: ', item, end=', ');
    print('\n');
    for item in lacos:
        print('\nO(s) local(s) de laços é: %d %d [lin][col]' % ((item + 1), (item + 1)), end=', ');
    print('\n');


    #resultado grafo regular
    if grafoRegular() == True:
        print('\nO grafo é regular.\n');
    else:
        print('\nO grafo não é regular.\n');

# checka se o grafo é regular ou não
def grafoRegular():
    # colocando o txt em uma matriz array
    matriz = open("./B.txt", "r");
    A = list();
    aux = 0;
    for line in matriz:
            A.append(list(map(int, line.split())));
    matriz.close();
    print(A);
    # varrendo a matriz A
    for line in A:
        for col in range(len(A) - 1): # verificando se o grafo não tem laços e as arestas são iguais
            if ((line[col] == line[col + 1]) and (col != aux)) or (line[col] == 0 and (col == aux)):
                print(line[col], aux)
                check = True;
            else:
                check = False;
        aux = aux + 1;
    if check == true:
        return True;
    else:
        return False;
    # se a diagonal principal for diferente de zero, todos os elementos tem que ser iguais
    # se a diagonal principal for igual a zero, todos os elementos tem que ser iguais, com exceção do elemento na diagonal principal


if __name__ == '__main__':
    main()