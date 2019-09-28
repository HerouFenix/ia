#Funcoes Recursivas para Processamento de Listas

#1.  Dada uma lista, retorna o seu comprimento.
def comprimento(list):
    if len(list) == 0:
        return 0
    return 1 + comprimento(list[1:])

#2.  Dada uma lista de n números, retorna a respectiva soma.
def  sum_list(list):
    if len(list) == 0:
        return 0
    return list[0] + sum_list(list[1:])

#3. Dada uma lista e um elemento, verifica se o elemento ocorre na lista.  Retorna um valorbooleano.
'''def check_elem(list,n):
    if len(list) == 0:
        return False
    elif list[0] == n:
        return True
    return check_elem(list[1:],n)'''

#3 [SOL. ALTERNATIVA]. Dada uma lista e um elemento, verifica se o elemento ocorre na lista.  Retorna um valorbooleano.
def check_elem(list,n):
    if not list:
        return False
    return list[0] == n or check_elem(list[1:],n)

#4.  Dadas duas listas, retorna a sua concatenaçao
def concat_lists(list1,list2):
    if list1 == []:
        return list2
    if list2 == []:
        return list1
    
    list1.append(list2[0])
    return concat_lists(list1,list2[1:])


#4 [SOL. SEM RECORSIVIDADE].  Dadas duas listas, retorna a sua concatenaçao
'''def concat_lists(list1,list2):
    aux = list1[:]
    aux[0:0] = list2
    return aux'''

#5.  Dada uma lista, retorna a sua inversa.
def inverse_list(list):
    if len(list) == 0:
        return []
    return inverse_list(list[1:]) + [list[0]]

#6.  Dada uma lista, verifica se forma uma capicua, ou seja, se, quer se leia da esquerda para adireita ou vice-versa, se obtem a mesma sequˆencia de elementos.
def capicua(list):
    if len(list) == 0:
        return True
    if list[0] == list[-1]:
        return capicua(list[1:-1])
    return False

#7.  Dada uma lista de listas, retorna a concatenaçao dessas listas.
def list_of_list_concat(lista):
    if len(lista) == 0:
        return []
    
    if not isinstance(lista[0],list): #This means that we do not have a list of lists anymore, so we can stop
        return lista

    return list_of_list_concat(lista[1:] + lista[0]) #Append the unlisted values of the first list in the list of lists to the end of the list of lists, and go deeper

#8. Dada uma lista, um elemento x e outro elemento y, retorna uma lista similar a lista de entrada, na qual x e substituido por y em todas as ocorrencias de x.
def replace_x_y_list(lista,x,y):
    if len(lista) == 0:
        return []
    
    if lista[0] == x:
        lista[0] = y
     
    lista = [lista[0]] + replace_x_y_list(lista[1:],x,y)

    return lista
    
#9. Dadas duas listas ordenadas de numeros, calcular a uniao ordenada mantendo eventuais repeticoes.
def ordered_union(lista1,lista2):
    if len(lista1) == 0:
        return lista2
    if len(lista2) == 0:
        return lista1
    
    sort_starters = lambda x,y: [min(x,y),max(x,y)]
    
    return sort_starters(lista1[0], lista2[0]) + ordered_union(lista1[1:], lista2[1:])

#10. Dado um conjunto, na forma de uma lista, retorna uma lista de listas que representa o conjunto de todos os subconjuntos do conjunto dado.
def combinations(lista): #Tricky one!!!
    if len(lista) == 0:
        return [[]]

    aux = combinations(lista[1:])

    return aux + [[lista[0]] + combination for combination in aux]





if __name__ == "__main__":
    #1.
    print("1) " + str(comprimento([1,2,3])))
    
    #2
    print("2) " + str(sum_list([1,2,3])))

    #3
    print("3) " + str(check_elem([1,2,3],4)))

    #4
    print("4) " + str(concat_lists([1,2],[3])))

    #5
    print("5) " + str(inverse_list([1,2,3])))

    #6
    print("6) " + str(capicua([1,2,3,2,1])))

    #7
    print("7) " + str(list_of_list_concat([[1,2,3],[4,5,6],[7,8,9]])))

    #8
    print("8) " + str(replace_x_y_list([1,2,1,3,1,1,4],1,8)))

    #9
    print("9) " + str(ordered_union([1,3,5],[2,4,6])))

    #10
    print("10) " + str(combinations([1,2,3])))