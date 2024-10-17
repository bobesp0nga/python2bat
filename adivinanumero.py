import random

minimo = 1
maximo = 10

numero = random.randit(minimo, maximo)

numeroadivinado = int(input(f"Dime un numero entre el {minimo} y {maximo}" ))

if numero==numeroadivinado:
    print("Enhorbuena, has acertado")
else:
    print("La has cagado")