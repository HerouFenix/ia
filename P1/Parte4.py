import math

#Expressoes Lambda e Expressoes de Ordem Superior

if __name__ == "__main__":
    #1. Dado um numero inteiro, retornaTruecaso o n ́umero seja  ́ımpar, eFalsecaso contrario
    odd = lambda n: n%2 != 0
    print(odd(1))

    #2. Dado um numero, retornaTruecasoo n ́umero seja positivo, eFalsecaso contrario.
    positivo = lambda n: n>0
    print(positivo(-2))

    #3. Dados  dois  numeros,x e y,  retornaTruecaso|x|<|y|, e False caso contrario.
    bigger = lambda x,y: abs(x) < abs(y)
    print(bigger(5,-6))

    #4. Dado  um  par  (x,y),  representandocoordenadas cartesianas de um ponto no planoXY, retorna um par (r,θ), correspondente`as coordenadas polares do mesmo ponto.
    polar = lambda x,y: (math.sqrt(x*x+y*y), math.atan2(y,x)) #Formula na wikipedia lmao
    print(polar(2,2))

    #5. Dadas tres funcoes de duas entradas,f,g e h, retorna uma funcao de tres entradas, x, y e z, cujo resultado e dado por: h(f(x,y),g(y,z).
    