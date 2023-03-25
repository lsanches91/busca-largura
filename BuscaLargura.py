grafo = {
    "A": ['C','J'],
    'B': ['C','F'],
    'C': ['A','B','F'],
    'D': ['G','M'],
    'E': ['H','I'],
    'F': ['B','C','H'],
    'G': ['D','J'],
    'H': ['E','F','J','K'],
    'I': ['E','K'],
    'J': ['A','G','H','M'],
    'K': ['H','I','L'],
    'L': ['K'],
    'M': ['D','J']
}

visitados = []
pilhaAux = []

#Confirmar se está correto pois ao buscar o D o M não foi impresso antes

def buscaLargura(raiz, procurado):
    if raiz == procurado:
        print('Valor encontrado.')
        return
    else:
        if raiz not in visitados:
            print('->' + raiz)
            visitados.append(raiz)
        
        for i in grafo[raiz]:
            if i not in visitados:
                visitados.append(i)
                pilhaAux.append(i)
                print('->' + i)
                if i == procurado:
                    print('Valor encontrado.')
                    return                
        if len(pilhaAux) != 0:
            return buscaLargura(pilhaAux.pop(0), procurado)
        else:
            print('Valor não encontrado.')
            return
        


if __name__ == '__main__':
    
    busca = input('Digite o valor que quer buscar: ')
    
    buscaLargura('H', busca)

    print(visitados)
    