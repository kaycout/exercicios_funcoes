# criar uma função que receba uma string e retorne a mesma string invertida.

def inverter_para_string(s):
    return s[::-1]

texto = ("oi kay, tudo bem? não morra quando o professor Edilson te chamar.")
texto_invertido = inverter_para_string(texto)
print(texto_invertido)