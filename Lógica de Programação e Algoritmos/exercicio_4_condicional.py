ladoA = int(input("Digite o ladoA"))
ladoB = int(input("digite o ladoB"))
ladoC = int(input("digite o ladoC"))

if((ladoA+ladoB)>ladoC and (ladoA+ladoC)>ladoB and (ladoB+ladoC)>ladoA):
    if(ladoA == ladoB and ladoB == ladoC and ladoA == ladoC):
        print("Equilátero")
    elif(ladoA != ladoB and ladoB != ladoC and ladoA != ladoC):
        print("Escaleno")
else:
    print("Isóceles")

    