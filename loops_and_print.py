def enumerate_list(list):
    lista_1 = []
    lista_2 = []
    for element in list:
        if element != "":
            lista_1.append(element)
            print(lista_1)
    for index in range(len(lista_1)):
            lista_2.append(f"{index}. {lista_1[index]}")
    return lista_2


def enumerate_backwards(list):
    lista_1 = []
    lista_2 = []
    for element in list:
        if element != "":
             lista_1.append(element[::-1])
             print(lista_1)
    for index in range(len(lista_1)):
         lista_2.append(f"{index}. {lista_1[index]}")
    return lista_2
