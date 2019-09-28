#Funçoes que retornam None

#1. Dada uma lista, retornar o elemento que esta a cabeca (ou seja, na posicao 0).
def get_head(lista): #( ͡° ͜ʖ ͡°)
    if len(lista) == 0: #No caso de lista vazia
        return None
    return lista[0]

#2. Dada uma lista, retornar a sua cauda (ou seja, todos os elementos a excepcao do primeiro).
def get_tail(lista):
    if len(lista) == 0: #No caso de lista vazia
        return None
    return lista[1:]

#3.  Dado um par de listas com igual comprimento, produzir uma lista dos pares dos elementos hoḿologos. (P.ex [1,2,3], [4,5,6] -> [(1,4),(2,5),(3,6])
def join_homologos(list1,list2):
    if len(list1) != len(list2): #Se n tiverem comprimento igual R.I.P
        return None
    if len(list1) == 0: #Se uma delas tiver comp 0 (a outra tmb tem) e estamos num caso limite (return lista vazia)
        return []
    
    return [(list1[0],list2[0])] + join_homologos(list1[1:],list2[1:]) #Criar o tuplo da cabeca de cada uma das listas e dar append da proxima iteracao

#4. Dada uma lista de numeros, retorna o menor elemento.
def get_smallest(lista):
    if len(lista) == 0: #No caso de lista vazia
        return None
    return min(lista)

#5. Dada uma lista de numeros, retorna um par formado pelo menor elemento e pela lista dos restantes elementos.
def get_smallest_and_rest(lista):
    if len(lista) == 0: #No caso de lista vazia
        return None
    
    smallest = min(lista)
    return [smallest, [element for element in lista if element != smallest] ] #Used List Comprehension :O

#6. Dada uma lista de numeros, calcular o maximo e o mınimo, retornando-os num tuplo.
def get_smallest_and_biggest(lista):
    if len(lista) == 0: #No caso de lista vazia
        return None
    
    return (min(lista),max(lista))

#7. Dada uma lista de numeros, retorna um triplo formado pelos dois menores elementos e pela lista dos restantes elementos.
def get_smallest_biggest_and_rest(lista):
    if len(lista) == 0: #No caso de lista vazia
        return None

    smallest = min(lista)
    biggest = max(lista)

    return (smallest,biggest, [element for element in lista if element != smallest and element != biggest])

#8. Dada uma lista ordenada de numeros, calcular se possıvel a respectiva media e mediana, retornando-as num tuplo.
def get_average_and_median(lista):
    if len(lista) == 0: #No caso de lista vazia
        return None
    if len([element for element in lista if isinstance(element, str)]) != 0: #Verificar se a lista é apenas numerica
        return None

    if lista != sorted(lista): #Verificar se a lista esta ordenada
        return None
        
    median = lista[len(lista)//2]

    sum = 0
    for i in lista:
        sum += i
    
    average = sum/len(lista)

    return (average,median)

if __name__ == "__main__":
    #1
    print("1) " + str(get_head([1,2,3])))
    print("1) " + str(get_head([])))

    #2
    print("2) " + str(get_tail([1,2,3])))
    print("2) " + str(get_tail([])))

    #3
    print("3) " + str(join_homologos([1,2,3],[3,2,1])))
    print("3) " + str(join_homologos([1,2,3],[3,1])))

    #4
    print("4) " + str(get_smallest([1,2,3])))
    print("4) " + str(get_smallest([])))
    
    #5
    print("5) " + str(get_smallest_and_rest([1,2,3])))
    print("5) " + str(get_smallest_and_rest([])))

    #6
    print("6) " + str(get_smallest_and_biggest([1,2,3,4])))
    print("6) " + str(get_smallest_and_biggest([])))

    #7
    print("7) " + str(get_smallest_biggest_and_rest([1,2,3,4])))
    print("7) " + str(get_smallest_biggest_and_rest([])))

    #8
    print("8) " + str(get_average_and_median([1,2,3,4,4,5,5])))
    print("8) " + str(get_average_and_median([1,3,4,2])))
    print("8) " + str(get_average_and_median([])))
    print("8) " + str(get_average_and_median([1,3,'b'])))
