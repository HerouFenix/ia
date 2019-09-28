#Funçoes para Processamento de Listas e Tuplos

#1.  Dada uma lista de pares, produzir um par com as listas dos primeiros e segundos elementos desses pares.
# separar ([(a1, b1),  ... (an, bn)]) = ([a1,  ... an], [b1, ... bn]
def separar(list):
    if list == []:
        return [], []
    a,b = list[0] #Get current iteration's element 1 and element 2

    listA, listB = separar(list[1:]) #Get a list of all next iteration's element1's and element2's
    return [a]+listA, [b]+listB #Append current to all next ones


#2.  Dada uma lista l e um elemento x, retorna um par formado pela lista dos elementos deldiferentes dexe pelo n ́umero de ocorrencias x em l.
def remove_and_count(list,elem):
    if list == []:
        return [], 0

    listResult, count = remove_and_count(list[1:],elem) #Get next counts and list result of next iterations
    if list[0] == elem:
        return listResult, count+1 #Add 1 if current elem in list is the same as the one we wanna count
    else:
        return [list[0]] + listResult, count #Add to the list result the current one (because we dont wanna remove it)


if __name__ == "__main__":
    #1
    print(separar([[1,2],[3,4],[5,6]]))

    #2
    print(remove_and_count([1,3,2,3,3,3],3))
