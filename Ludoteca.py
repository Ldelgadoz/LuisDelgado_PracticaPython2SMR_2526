juegos = [["Catan", 4],["Dixit",2],["Virus",6],["Carcassonne",3]]
opcion = ""

while (opcion != "s"):
    print ("---LUDOTECA---")
    print (" a) Añade un juego")
    print (" b) Mostrar lista de juegos")
    print (" c) Mostrar lista de juegos ordenada (de la Z a la A)")
    print (" d) Mostrar lista de juegos de menor a mayor")
    print (" e) Elimina un juego")
    print (" f) Aplicar mantenimiento")
    print (" s) Salir")
    opcion = input ("Introduce la opción: ")

    if opcion == "a":
        juego = input ("Introduce el nombre del juego: ")
        unidades = float (input ("Introduce las unidades del juego:"))
        juegos.append[[juego, unidades]]
    elif opcion == "b":
        print ("Esta es la lista de juegos ", juegos)
    elif opcion == "c":
        juegosZA = sorted ( juegos,  key=lambda x: x[0], reverse=True)
        print ("La lista de juegos ordenada de la Z a la a quedaria asi", juegosZA)
    elif opcion == "d":
        juegosmenmay = sorted ( juegos,  key=lambda x: x[1] )
        print ("Los juegos ordenados de mayor unidades a menor serian estos ", juegosmenmay)
    elif opcion == "e":
        juegoborrar = input ("Que juego quieres borrar?: ")
        lista_borrar = []
        for elemento in juegos:
            if elemento[0]== juegoborrar():
                lista_borrar.append(elemento)
            for i in lista_borrar:
                juegos.remove(i)
                print ("El juego ", i, "ha sido eliminado")

    elif opcion == "s":
        print ("Hasta luego.")
    else:
        print("Eso no es una opción valida")
            