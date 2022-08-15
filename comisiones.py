porcent_comision = 13
ventas = int(input("Número de ventas "))
nombre = input("¿Cómo te llamas? ")

total_comision = round(ventas * 13 / 100, 2)

print("Hola {}, el total de comisión este es es de {}".format(nombre, total_comision))
