import re

def replace_colors(input_path, colors_path, output_path):
    # Cargar la lista de colores en un diccionario
    colors_dict = {}
    with open(colors_path, 'r') as colors_file:
        for line in colors_file:
            old_color, new_color = line.strip().split(' = ')
            colors_dict[old_color] = new_color

    # Abrir y leer el archivo de entrada
    with open(input_path, 'r') as input_file:
        content = input_file.read()

    # Reemplazar los colores utilizando expresiones regulares
    for old_color, new_color in colors_dict.items():
        # Buscar colores en minúsculas o mayúsculas con expresiones regulares
        pattern = re.compile(re.escape(old_color), re.IGNORECASE)
        content = pattern.sub(new_color, content)

    # Guardar el contenido modificado en el archivo de salida
    with open(output_path, 'w') as output_file:
        output_file.write(content)

# Solicitar rutas de archivos al usuario
input_path = input("Ruta del archivo a modificar: ")
colors_path = input("Ruta de la lista de colores: ")
output_path = input("Ruta para guardar el archivo modificado: ")

# Llamar a la función para reemplazar colores
replace_colors(input_path, colors_path, output_path)
print("Reemplazo de colores completado. El archivo ha sido guardado.")
