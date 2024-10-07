# AND = para ser TRUE tudo tem que ser TRUE
# OR = para ser TRUE apenas um tem que ser TRUE

print (True and True)
print (True and False)
print (False and False)
print (True or True)
print (True or False)
print (False or False)

saldo = 1000
saque = 200
limite = 100
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)