# def é para definir uma função

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Pedro"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem() #Assim funciona
#exibir_mensagem_2(nome)
exibir_mensagem_3() #Assim funciona
exibir_mensagem_3(nome="Augusto") #Assim funciona