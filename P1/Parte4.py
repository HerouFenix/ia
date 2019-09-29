import math

#Expressoes Lambda e Expressoes de Ordem Superior

if __name__ == "__main__":
    #1. Dado um numero inteiro, retorna True caso o ńumero seja  ́ımpar, e False caso contrario
    odd = lambda n: n%2 != 0
    print("1) " + str(odd(1)))

    #2. Dado um numero, retorna True casoo ńumero seja positivo, e False caso contrario.
    positivo = lambda n: n>0
    print("2) " + str(positivo(-2)))

    #3. Dados  dois  numeros,x e y,  retorna True caso |x|<|y|, e False caso contrario.
    bigger = lambda x,y: abs(x) < abs(y)
    print("3) " + str(bigger(5,-6)))

    #4. Dado  um  par  (x,y),  representandocoordenadas cartesianas de um ponto no plano X Y, retorna um par (r,θ), correspondente as coordenadas polares do mesmo ponto.
    polar = lambda x,y: (math.sqrt(x*x+y*y), math.atan2(y,x)) #Formula na wikipedia lmao
    print("4) " + str(polar(2,2)))

    #5. Dadas tres funcoes de duas entradas,f,g e h, retorna uma funcao de tres entradas, x, y e z, cujo resultado e dado por: h(f(x,y),g(y,z).
    #Portanto, temos 3 funçoes com parametros x,y e z (funcao f, g e h) e uma funçao que vai aceitar as 3 funçoes como parametros e retornar o resultado de h(f(x,y),g(y,z)
    f = lambda x,y: x*y
    g = lambda x,y: pow(x,y)
    h = lambda x,y: x>y

    trenaria = lambda f,g,h: h(f(2,3),g(2,3))
    print("5) " + str(trenaria(f,g,h)))

    #Nota: Perguntar se era isto q o exercicio estava a pedir! :/

    #6. Dada uma lista e uma funcao booleana unaria, retorna True caso a funcao tambem retorne True para todos os elementos da lista, e False caso contrario. ( Quantiﬁcador universal )

    check_positive = lambda x: x>0
    check_true_all = lambda lista,checker: True if len(lista) == 0 else checker(lista[0]) and check_true_all(lista[1:],checker)
    print("6) " + str(check_true_all([1,2,3],check_positive)))
    print("6) " + str(check_true_all([1,-2,3],check_positive)))

    #7. Dada uma lista e uma funcao booleana unaria, retorna True caso a funcao retorne True para pelo menos um dos elementos da lista, e False caso contrario. ( Quantiﬁcador existencial )

    check_true_one = lambda lista,checker: False if len(lista) == 0 else checker(lista[0]) or check_true_one(lista[1:],checker)
    print("7) " + str(check_true_one([1,2,3],check_positive)))
    print("7) " + str(check_true_one([-1,2,-3],check_positive)))
    print("7) " + str(check_true_one([-1,-2,-3],check_positive)))
