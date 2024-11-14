# função que receba uma lista de números e retorne
# a média aritmética.

def calcular_media(lista):
    if len(lista) == 0:
        return 0
    soma = sum(lista)
    media = soma /len(lista)
    return media

    
numeros = [15, 90, 40, 60, 50]
media = calcular_media(numeros)
print(media)

numeros_vazio = []
media_vazia = calcular_media(numeros_vazio)
print(media_vazia)
