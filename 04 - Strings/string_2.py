nome = 'Pedro'
idade = 27
profissao = 'Analista'
linguagem = 'Python'
saldo = 45.435

dados = {'nome': 'Pedro', 'idade': 28}

print('Nome: %s\nIdade: %d' % (nome, idade))
print('Nome: {}\nIdade: {}'.format(nome, idade))
print('Nome: {0}\nIdade: {1}'.format(nome, idade))
print('Nome: {nome}\nIdade: {idade}'.format(nome=nome, idade=idade))
print('Nome: {name}\nIdade: {age}'.format(name=nome, age=idade))
print('Nome: {nome}\nIdade: {idade}'.format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")