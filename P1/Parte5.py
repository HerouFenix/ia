#Ordenacao de listas

#1. Dada uma lista, retornar o elemento que esta a cabeca (ou seja, na posicao 0).
def algorithmic_sort(lista,type): 
    if type == 1: #Selection Sort
        for i in range(len(lista)): 
            # Find the minimum element in remaining  
            # unsorted array 
            min_idx = i 
            for j in range(i+1, len(lista)): 
                if lista[min_idx] > lista[j]: 
                    min_idx = j 
                    
            # Swap the found minimum element with  
            # the first element         
            lista[i], lista[min_idx] = lista[min_idx], lista[i] 
        return lista
        
    if type == 2: #Bubble Sort
        for i in range(len(lista)):
            # Last i elements are already in place
            for j in range(0, len(lista)-i-1):
    
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if lista[j] > lista[j+1] :
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    if type == 3: #Quick Sort
        return quicksort(lista)

    return None 
    
#Quick Sort Functions#
def quicksort(lista):
    lesser = []
    equal = []
    greater = []

    if len(lista) > 1:
        pivot = lista[0]
        for x in lista:
            if x < pivot:
                lesser.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quicksort(lesser)+equal+quicksort(greater)

    else: 
        return lista
######################

#2. Similar ao numero anterior, mas sem restricao no tipo dos elementos da lista de entrada. A funcao de ordenacao recebe, num parametro adicional, a rela¸cao de ordem (uma funcao binaria booleana para comparacao elemento a elemento) segundo a qual a lista de entrada deve ser ordenada.

def algorithmic_sort_2(lista,type,compare): 
    if type == 1: #Selection Sort
        for i in range(len(lista)): 
            # Find the minimum element in remaining  
            # unsorted array 
            min_idx = i 
            for j in range(i+1, len(lista)): 
                if compare(lista[min_idx],lista[j]): 
                    min_idx = j 
                    
            # Swap the found minimum element with  
            # the first element         
            lista[i], lista[min_idx] = lista[min_idx], lista[i] 
        return lista
        
    if type == 2: #Bubble Sort
        for i in range(len(lista)):
            # Last i elements are already in place
            for j in range(0, len(lista)-i-1):
    
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if compare(lista[j],lista[j+1]) :
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    if type == 3: #Quick Sort
        return quicksort2(lista,compare)

    return None 
    
#Quick Sort Functions#
def quicksort2(lista,compare):
    la = []
    equal = []
    lb = []

    if len(lista) > 1:
        pivot = lista[0]
        for x in lista:
            if compare(x,pivot):
                lb.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                la.append(x)
        return quicksort2(la,compare)+equal+quicksort2(lb,compare)

    else: 
        return lista
######################



if __name__ == "__main__":
    #1
    print("1) " + str(algorithmic_sort([3,2,5,1,4],1)))
    print("1) " + str(algorithmic_sort([3,2,5,1,4],2)))
    print("1) " + str(algorithmic_sort([3,2,5,1,4],3)))

    #2
    comparassion = lambda x,y: x<y
    print("2) " + str(algorithmic_sort_2([3,2,5,1,4],1,comparassion)))
    print("2) " + str(algorithmic_sort_2([3,2,5,1,4],2,comparassion)))
    print("2) " + str(algorithmic_sort_2([3,2,5,1,4],3,comparassion)))

    