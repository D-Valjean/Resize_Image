import os
from PIL import Image

base_width = 800

def resize_image(file_path):
    img = Image.open(file_path)
    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
    
    # Change the extension to .webp
    new_file_path = os.path.join(os.path.dirname(file_path), f"New_{os.path.splitext(os.path.basename(file_path))[0]}.webp")
    img.save(new_file_path)

# Ruta del directorio que contiene las imágenes
directory = 'C:\\Users\\Frank\\OneDrive\\Documents\\Lote 4'

# Recorremos todos los archivos en el directorio
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path) and file_name.endswith(('.png', '.jpeg', '.jpg', '.webp', '.jfif')):
        resize_image(file_path)