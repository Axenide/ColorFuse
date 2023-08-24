# "ColorFuse" by Axenide >>> https://github.com/Axenide/ColorFuse

import re
import os
import shutil

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return "#{:02X}{:02X}{:02X}".format(*rgb_color)

def calculate_midpoint_color(color1, color2):
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    midpoint_rgb = tuple((c1 + c2) // 2 for c1, c2 in zip(rgb1, rgb2))
    return rgb_to_hex(midpoint_rgb).lower()

def replace_colors_in_file(file_path, new_colors):
    with open(file_path, 'r+') as file:
        content = file.read()
        hex_pattern = r'#[A-Fa-f0-9]{6}|[A-Fa-f0-9]{6}'
        colors = re.findall(hex_pattern, content)
        
        for new_color in new_colors:
            if colors:
                content = content.replace(colors.pop(0), new_color, 1)
        
        file.seek(0)
        file.truncate()
        file.write(content)

if __name__ == "__main__":
    file1_path = input("First file path: ")
    file2_path = input("Second file path: ")

    with open(file1_path, 'r') as file1:
        content1 = file1.read()
    colors1 = re.findall(r'#[A-Fa-f0-9]{6}|[A-Fa-f0-9]{6}', content1)

    with open(file2_path, 'r') as file2:
        content2 = file2.read()
    colors2 = re.findall(r'#[A-Fa-f0-9]{6}|[A-Fa-f0-9]{6}', content2)

    new_colors = []
    output_file_path = input("Fusion path: ")
    
    for color1, color2 in zip(colors1, colors2):
        new_color = calculate_midpoint_color(color1, color2)
        new_colors.append(new_color)
    
    output_base_name = os.path.splitext(os.path.basename(output_file_path))[0]
    output_directory = os.path.dirname(output_file_path)  # Obtener la ruta del directorio
    
    colors_output_path = os.path.join(output_directory, f"{output_base_name}.colors")
    
    with open(colors_output_path, 'w') as colors_file:
        for color1, color2, new_color in zip(colors1, colors2, new_colors):
            colors_file.write(f"{color1} + {color2} = {new_color}\n")
    
    shutil.copyfile(file1_path, output_file_path)
    replace_colors_in_file(output_file_path, new_colors)

    print(f"Colors fused into {output_file_path}!")
    print(f"Fused colors listed in {colors_output_path}")
