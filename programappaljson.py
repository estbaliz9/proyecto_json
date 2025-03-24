import tim
import funcionesjson

ruta = "json_disney.json"


datos = funcionesjson.leer_json(ruta)

menu = '''
🎬​​ CINE DE DISNEY ​🎬​ 

1. Ver la cartelera.
2. Personajes por película.
3. Consultar películas según su duracion.
4. Buscar película indicando el personaje.
5. Películas más premiadas por plataforma.
6. Salir.

    => Selecciona una opción: '''

opcion = int(input(menu))
   
while opcion !=6:
    if opcion == 1:
        funcionesjson.listar_peliculas(datos)
    elif opcion == 2:
        funcionesjson.contar_personajes(datos)
    elif opcion == 3:
        funcionesjson.filtrar_por_duracion(datos)
    elif opcion == 4:
        funcionesjson.buscar_por_personaje(datos)
    elif opcion == 5:
        funcionesjson.peliculas_mas_premiadas(datos)
        
    time.sleep(2)
    print("Cargando menú principal...")
    time.sleep(3)
    opcion = int(input(menu))

print("Cerrando puertas... ")
time.sleep(2)
print("📽 Esperemos que lo hayas pasado bien, hasta pronto !! 📽 ")
