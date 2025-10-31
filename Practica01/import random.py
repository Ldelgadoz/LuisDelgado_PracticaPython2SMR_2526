import random


usuarios = []
añadir = "si" 
while añadir.lower() == "si":
    nombre = input("Usuario: ")
    clave = input(f"Contraseña para {nombre}: ")
    usuarios.append([nombre, clave]) 
    añadir = input("¿Añadir más? (si/no): ")

claves_debiles = ["1234", "password", "qwerty", "abc123", "hola", "admin"]

vulnerados = []
nombres_originales = []
for u in usuarios:
    nombres_originales.append(u[0])

if len(usuarios) == 0:
    print("No hay usuarios. Fin.")
else:
    atacar = "si"
    print("\n--- INICIO SIMULACIÓN ---")

    while atacar.lower() == "si":
        print("\n--- Intento de Ataque ---")
        
        
        user_elegido = random.choice(usuarios)
        nombre_ataque = user_elegido[0]
        passw = user_elegido[1]

        vulnerado_ahora = False 

    
        for debil in claves_debiles:
            if passw.lower() == debil:
                print(f"¡VULNERADO! Usuario {nombre_ataque}. Contraseña débil: '{passw}'")

                
                ya_vulnerado = False 
                for v in vulnerados:
                    if v == nombre_ataque:
                        ya_vulnerado = True
                
                if ya_vulnerado == False:
                    vulnerados.append(nombre_ataque) 

                vulnerado_ahora = True
                break

        if vulnerado_ahora == False:
            print(f"RESISTIÓ. Usuario {nombre_ataque} seguro en este intento.")

        atacar = input("\n¿Otro ataque? (si/no): ")

    
    print("\n" + "="*30)
    print("--- RESUMEN ---")
    print("="*30)

    resistentes = []
    
    
    for n in nombres_originales:
        fue_vulnerado = False 
        for v in vulnerados:
            if n == v:
                fue_vulnerado = True
        
        if fue_vulnerado == False:
            resistentes.append(n)

    print(f"Vulnerados ({len(vulnerados)}): {', '.join(vulnerados)}")
    print(f"Resistentes ({len(resistentes)}): {', '.join(resistentes)}")
    print("="*30)