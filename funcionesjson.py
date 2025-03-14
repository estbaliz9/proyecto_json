documento = "json_disney.json"
import json

def leer_json(documento):
    with open(documento, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return datos

# 1. Listar información
def listar_peliculas(datos):
    print('''
Las películas disponibles para ver, son:
''')
    for pelicula in datos:
        print("📽 ", pelicula['Titulo'], "(", pelicula['AñoEstreno'],") , " ,pelicula['DuracionMin'], " min")

# 2. Contar información
def contar_personajes(datos):
    print("Las películas que tenemos en cartelera y sus personajes son los siguientes: ")
    for pelicula in datos:
        num_personajes = len(pelicula['Personajes'])
        print("📽 ", pelicula['Titulo'], " hay ", num_personajes, "personajes.")

# 3. Buscar o filtrar por duración
def filtrar_por_duracion(datos):
    min_duracion = int(input("Dime la mínima duración en minutos:  "))
    max_duracion = int(input("Dime la máxima duración en minutos: "))
    print("Las películas que tenemos con una duracion entre " , min_duracion, " y ", max_duracion, " minutos, son: ")
    for pelicula in datos:
        if min_duracion <= pelicula['DuracionMin'] <= max_duracion:
             print("📽", pelicula['Titulo'], " su duración es ", pelicula['DuracionMin'], " minutos.")
        else:
            print("No hay ninguna película con esa duracion, intentelo de nuevo. ")

# 4. Buscar película por personaje
def buscar_por_personaje(datos):
    personaje = input("Ingrese el nombre del personaje: ")
    print("Las películas donde aparece", personaje, "son: ")
    encontrado = False
    for pelicula in datos:
        for var in pelicula['Personajes']:
            if var['Nombre'].lower() == personaje.lower():
                print("📽 ", pelicula['Titulo'])
                encontrado = True  # Actualizar el flag cuando se encuentra una coincidencia
    if not encontrado:
        print("No se encontró ninguna película con ese personaje.")

# 5. Lista películas con más premios por plataforma
def peliculas_mas_premiadas(datos):
    plataformas = {}
    for pelicula in datos:
        total_premios = pelicula['Premios']['Oscars'] + pelicula['Premios']['GoldenGlobes'] + pelicula['Premios']['AnnieAwards']
        for plataforma in pelicula['Plataformas']:
            if plataforma not in plataformas or total_premios > plataformas[plataforma]['premios']:
                plataformas[plataforma] = {
                    'titulo': pelicula['Titulo'],
                    'premios': total_premios}
    print("Películas con más premios por plataforma:")
    for plataforma, info in plataformas.items():
        print("En ", plataforma, " la película ", info['titulo'], " tiene ", info['premios'], " premios. ")
