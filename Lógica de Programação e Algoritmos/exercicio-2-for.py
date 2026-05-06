inicio = int(input("Digite o número de inicio:"))
fim = int(input("Digite o número final:"))
soma=0

for i in range(inicio, fim+1):
    if(i%2 == 0):
        soma = soma + i

print(soma)