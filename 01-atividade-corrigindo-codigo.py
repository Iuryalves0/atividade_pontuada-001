import os
os.system("cls || clear")


#Quantidade de numeros a serem utilizados
quantidade_numeros =  6

# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0
lista_numeros = [ ]


# Variáveis para armazenar os números
for i in range(quantidade_numeros):
    numero = int(input(f"Digite o {i+1}º número: "))
    soma_geral +=  numero
    lista_numeros.append(numero)
    
    #verificando se são impares ou pares

    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero


#verificando se os numeros são positivos ou negativos
    
    if numero > 0:
        quantidade_positivos +=1
    else:
        quantidade_negativos +=1

#verificando maior e menor
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

#Media Geral
media_geral = soma_geral/quantidade_numeros
#media dos numeros pares e impares
media_pares = soma_pares/quantidade_pares
media_impares = soma_impares/quantidade_impares
# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares}")
print(f"Média dos números ímpares: {media_impares}")
print(f"Média de todos os números:{media_geral} ")
print("==== Números na ordem inversa =====")
for numero in reversed(lista_numeros):
    print(numero)