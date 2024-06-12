import math


# Paso 1: Solicitar al usaurio que ingrese el radio del círculo que quiere calcular
radio = float(input("Por favor ingrese el radio del círculo: "))

# Paso 2: Calcular el área del círculo utilizando la fórmula "area = pi x radio^2"
area = math.pi * (radio ** 2)

# Paso 3: Mostrar al usaurio el área calculada
print ("El área del círculo con radio", radio, "es", area)

