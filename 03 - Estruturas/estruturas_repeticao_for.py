texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else: # não é muito utilizada no dia a dia com for
    print() # adicona uma quebra de linha
    print("Executa no final do laço")

# exemplo utilizando a função built-in range
for numero in range (0,51,5):
    print(numero, end=" ")