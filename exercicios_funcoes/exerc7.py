# faça uma função que receba uma lista e retorne uma nova lista
# com os elementos pares da lista original.

def filtrar_pares(lista):
    return [x for x in lista if x % 2 == 0]
lista_original = [1,2,3,4,5,6,7,8,9]
lista_pares = filtrar_pares(lista_original)
print(lista_pares)