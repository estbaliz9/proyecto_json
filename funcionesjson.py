documento = "json_disney.json"
import json

#PARA LEER FICHERO
def leer_json(documento):
    with open(documento, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return datos

# 1. LISTAR INFORMACIÓN
def listar_peliculas(datos):
    print(" 🪄​ Las películas disponibles para ver son:")

    # el ancho máximo de cada columna
    max_titulo = max(len(pelicula['Titulo']) for pelicula in datos) if datos else 10
    max_anio = 4  # los ños tienen siempre 4 dígitos
    max_duracion = max(len(str(pelicula['DuracionMin'])) for pelicula in datos) if datos else 10

    # encabezado tabla
    print("Título", " " * (max_titulo - len("Título")), " Año ", "Duración")
    print("=" * (max_titulo + max_anio + max_duracion + 10))

    # filas
    for pelicula in datos:
        espacios_titulo = " " * (max_titulo - len(pelicula['Titulo']))
        espacios_duracion = " " * (max_duracion - len(str(pelicula['DuracionMin'])))
        print(pelicula['Titulo'], espacios_titulo, pelicula['AñoEstreno'], espacios_duracion, pelicula['DuracionMin'], "min")

# 2. CONTAR
def contar_personajes(datos):
    print(" ​ ​❤️​ Las películas que tenemos en cartelera y sus personajes son los siguientes:")
    for pelicula in datos:
        num_personajes = len(pelicula['Personajes'])
        print("- ", pelicula['Titulo'], ": " , num_personajes , "personajes")


# 3. BUSCAR PELICULA POR DURACIÓN
def filtrar_por_duracion(datos):
    min_duracion = int(input("Duración en minutos:  "))
    max_duracion = int(input("Máxima duración en minutos: "))
    print("Las películas que tenemos con una duracion entre " , min_duracion, " y ", max_duracion, " minutos, son: ")

    # determinar el ancho 
    max_titulo = max(len(pelicula['Titulo']) for pelicula in datos) if datos else 10

    # encabezado 
    print("Título", " " * (max_titulo - len("Título")), "Duración ")
    print("=" * (max_titulo + 15))

    peliculas_filtradas = [pelicula for pelicula in datos if min_duracion <= pelicula['DuracionMin'] <= max_duracion]

    if peliculas_filtradas:
        for pelicula in peliculas_filtradas:
            espacios_titulo = " " * (max_titulo - len(pelicula['Titulo']))
            print(pelicula['Titulo'], espacios_titulo, pelicula['DuracionMin'], "min")
    else:
        print("No hay ninguna película con esa duración, inténtelo de nuevo.")


# 4. BUSCAR PELICULA POR NOMBRE
def buscar_por_personaje(datos):
    print(" ⚔️​ Lista de personajes disponibles:")
    personajes_unicos = set(var['Nombre'] for pelicula in datos for var in pelicula['Personajes'])
    for personaje in personajes_unicos:
        print("- ", personaje)

    personaje = input("Ingrese el nombre del personaje: ")
    print("Las películas donde aparece ", personaje, " son:")
    encontrado = False

    for pelicula in datos:
        for var in pelicula['Personajes']:
            if var['Nombre'].lower() == personaje.lower():
                print("📽 ", pelicula['Titulo'])
                encontrado = True  

    if not encontrado:
        print("No hay ninguna película con ese personaje, intentalo de nuevo.")


# 5. LISTA PELICULAS PREMIADAS
def peliculas_mas_premiadas(datos):
    plataformas = {}
    for pelicula in datos:
        total_premios = pelicula['Premios']['Oscars'] + pelicula['Premios']['GoldenGlobes'] + pelicula['Premios']['AnnieAwards']
        for plataforma in pelicula['Plataformas']:
            if plataforma not in plataformas or total_premios > plataformas[plataforma]['premios']:
                plataformas[plataforma] = {
                    'titulo': pelicula['Titulo'],
                    'premios': total_premios}
    print("Películas con más premios por plataforma: ")
    for plataforma, info in plataformas.items():
        print("En ", plataforma, " la película ", info['titulo'], " tiene ", info['premios'], " premios. ")

