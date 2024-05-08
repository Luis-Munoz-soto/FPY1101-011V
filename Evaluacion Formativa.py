
pikachu_roll = 4500
otaku1_roll = 5000
pulpo_venenoso_roll = 5200
anguila_electrica_roll = 4800
total_pedido = 0
total_pedido_mas_descuento = 0
val_producto = 0


mientras1 = 1
mientras2 = 2

print("--Bienbenido a nuestro local--")

while mientras1 == 1:

    print("Este es nuestro menu de productos:")
    print("1) Pikachu Roll Valor: $4.500")
    print("2) Otaku Roll Valor: $5.000")
    print("3) Pulpo Venenoso Roll Valor: $5.200")
    print("4) Anguila Electrica Roll Valor: $4.800")
    print("5) Terminar Pedido")

    op1 = int(input("Indiquenos que producto necesita: "))

    if op1 >= 6:
        print("La opcion tiene que ser entre 1 y 5")
        print("-----------------------------------------------")
    if op1 <= 0:
        print("La opcion tiene que ser entre 1 y 5")
        print("-----------------------------------------------")
    if op1 == 1:
        print("Seleccionaste la opcion 1: Pikachu Roll")
        val_producto = 4500
    if op1 == 2:
        print("Seleccionaste la opcion 2: Otaku Roll")
        val_producto = 5000
    if op1 == 3:
        print("Seleccionaste la opcion 3: Pulpo Venenoso Roll")
        val_producto = 5200
    if op1 == 4:
        print("Seleccionaste la opcion 4: Anguila Electrica Roll")
        val_producto = 4800
    if op1 == 5:
        mientras1 = 2

print(f"El valor total de su pedido es de {total_pedido}")





