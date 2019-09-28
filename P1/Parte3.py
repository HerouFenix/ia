#Funçoes que retornam None

#3.  Dado um par de listas com igual comprimento, produzir uma lista dos pares dos elementos hoḿologos. (P.ex [1,2,3], [4,5,6] -> [(1,4),(2,5),(3,6])
def join_homologos(list1,list2):
    if len(list1) != len(list2): #Se n tiverem comprimento igual R.I.P
        return None
    if len(list1) == 0: #Se uma delas tiver comp 0 (a outra tmb tem) e estamos num caso limite (return lista vazia)
        return []
    
    return [(list1[0],list2[0])] + join_homologos(list1[1:],list2[1:]) #Criar o tuplo da cabeca de cada uma das listas e dar append da proxima iteracao

if __name__ == "__main__":
    #3
    print(join_homologos([1,2,3],[3,2,1]))