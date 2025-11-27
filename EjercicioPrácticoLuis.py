catalogo = [
 ["Inception", "pelicula", "thriller", 5, 2010],
 ["One Piece", "serie", "anime", 4, 1999],
 ["La La Land", "pelicula", "romantica", 4, 2016],
 ["Stranger Things", "serie", "fantastica", 5, 2016],
 ["Superbad", "pelicula", "comedia", 4, 2007],
 ["La Comunidad del Anillo", "pelicula", "fantastica", 5, 2001]
    
    ]

opcion = ""
opcionb = ""
while (opcion != "d"):
    print("---CATALOGO---")
    print("a) Ver catálogo")
    print("b) Filtrar por género")
    print("c) Cambiar puntuación")
    print("d) Salir")
    opcion = input ("Que desde hacer?: ")
    if opcion == "a":
        print ("VER CATALOGO")
        print ("a) ordenar alfabeticamente por titulo")
        print ("b) ordenar por año (mas reciente a mas antigua)")
        opcionb = input ("Seleccione una opción: ")
        if opcionb == "a":
                catalogo.sort(key=lambda x: x[0])
                print ("aqui tienes la lista ordenada por titulo",catalogo)
    elif opcionb == "b":
        catalogo.sort(key=lambda x: x[4], reverse=True )   
        print ("aqui tienes la lista ordenada por año", catalogo)

    if opcion == "b":
        print ("ha seleccionado filtrar por genero")
        opciong = input ("Por favor indique que genero quiere buscar: ")
        print ("Usted ha seleccionado", opciong, "Buscando peliculas/series que tengan la opcion")
        for i in catalogo:
            opcion.sort(key=lambda x: x[2])
            print (catalogo)
    if opcion == "c":
        print("")
    if opcion == "d":
        print  ("¿¿Hasta luego!!")