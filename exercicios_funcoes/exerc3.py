# criar uma função que verifique se o número é par ou impar.
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

