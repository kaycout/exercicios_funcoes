# exercício 1

def soma(a, b):
    return a + b

resultado = soma (5, 3)
print(resultado)

# exercício 2

def celsius_para_fahrenheit(celsius):
    fahreinheit = (celsius)
    return fahreinheit

temperatura_celsius = (25)
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} °C é igual a {temperatura_fahrenheit}°F ")

# exercício 3

def verificar_par_ou_impar(numero):
    if numero% 2 == 0:
        return "Par"
    else:
        return "Impar"

# verifica se o número impar
numero = 7
resultado = verificar_par_ou_impar(numero)
print(f"O número {numero} é {resultado}.")

# verifica se o número é par
numero = 10
resultado = verificar_par_ou_impar(numero)
print(f"O número {numero} é {resultado}.")

# exercício 4

def inverter(s):
    return s[::-1]

texto = ("oi kay, tudo bem?")
texto_invertido = inverter(texto)
print(texto_invertido)

# len = quantidade
# len -1 = para ver a posição dos elementos 
# end "" = para mandar o texto invertido 
# criar variável que devolve o texto invertido
# txt_invertido=""

# exercício 6

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

# exercício 7

def filtrar_pares(lista):
    return [x for x in lista if x % 2 == 0]
lista_original = [1,2,3,4,5,6,7,8,9]
lista_pares = filtrar_pares(lista_original)
print(lista_pares)



