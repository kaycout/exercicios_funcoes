# função que receba uma string e retorne a mesma string invertida.

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