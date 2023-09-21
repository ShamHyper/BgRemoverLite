import os
import shutil
from clear import clear
from PIL import Image
from rembg import remove
from colors import *

color_start()
input_dir = "input"
output_dir = "output"
current_directory = os.path.dirname(os.path.abspath(__file__))

def rem_bg_def(): 
    pics = 0
    for filename in os.listdir(input_dir):
        pics += 1
        print(f"{y}[Лог|Картинка #{pics}]Удаляю фон с картинки... жди.")

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"{filename[:-4]}_output.png")

        if not filename.endswith(".png"):
            input_image = Image.open(input_path).convert("RGB")
            input_path = os.path.join(output_dir, f"{filename[:-4]}_input.png")
            input_image.save(input_path)
            print(f"{y}[Важно|Картинка #{pics}] Удаление фона с не .png картинок может привести к небольшому ухудшению качества.")

        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)

        print(f"{y}[Лог|Картинка #{pics}]Фон с картинки удалён. Едем дальше.")

    return pics

clear()

ask_auto_mode = input(f"{w}Хотите использовать изображения из папки input или укажите путь сами?\n[+]Режим папки input\n[-]Режим своего пути\nВведите ответ (+ или -): ") 

if ask_auto_mode == "+" or " ":
    auto_mode = True
if ask_auto_mode == "-":
    auto_mode = False
    print("")
    your_dir = input(f"{w}Введите путь к папке с картинкой/картинками.\nПример - D:/User/Img\nВведите путь: ")

if auto_mode == True:
    print("")
    print(f"{y}[Лог]Начинаю удаление фонов с картинок в режиме input...")
    pics = rem_bg_def()
if auto_mode == False:
    input_dir = os.path.abspath(your_dir)
    print("")
    print(f"{y}[Лог]Начинаю удаление фонов с картинок в папке: {your_dir}...")
    pics = rem_bg_def()

if pics == 0: 
    print("")
    print(f"{r}[Ошибка]Чтобы удалить фон с картинки, нужна картинка.")
if pics > 0:
    print("")
    print(f"{g}Готово! Удалены фоны с {pics} картинок.")

print("")
input(f"{w}Чтобы выйти из скрипта нажмите Enter...")

pycache_directory = os.path.join(current_directory, '__pycache__') # Удаление кеша
shutil.rmtree(pycache_directory)