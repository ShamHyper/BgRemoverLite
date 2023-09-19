import os
from rembg import remove
from PIL import Image

input_dir = "input"
output_dir = "output"

def clr(): 
    os.system('cls') 

def rem_bg_def():
    i = 0
    for filename in os.listdir(input_dir):
        i += 1
        print(f"[Лог|Картинка #{i}]Удаляю фон с картинки... жди.")

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"{filename[:-4]}_output.png")

        if not filename.endswith(".png"):
            input_image = Image.open(input_path).convert("RGB")
            input_path = os.path.join(output_dir, f"{filename[:-4]}_input.png")
            input_image.save(input_path)
            print(f"[Важно|Картинка #{i}] Удаление фона с не .png картинок может привести к небольшому ухудшению качества.")

        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)

        print(f"[Лог|Картинка #{i}]Фон с картинки удалён. Едем дальше.")

    return i