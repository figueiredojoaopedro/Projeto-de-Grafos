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

if __name__ == '__main__':
    main()