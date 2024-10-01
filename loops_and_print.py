def enuerate_list(lista):
    nl = []
    for i in range(len(lista)):
        nl.append(i)
        nl.append(lista[i])
        nl.append(",")

def enumerate_backwards(lista):
    nl=[]
    for i in range(len(lista)):
        r=lista[i][::-1]
        nl.append(i)
        nl.append(r)
    print(nl)
