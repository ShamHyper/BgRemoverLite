import os
import colorama
from PIL import Image
from rembg import *
from colors import *

colorama.init()

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

clr()

ask_auto_mode = input(f"{w}Хотите использовать изображения из папки input или укажите путь сами?\nЕсли нужен режим папки input, напишите + или нажмите Enter\nЕсли нужен режим пути, напишите -\nВведите ответ: ") 

if ask_auto_mode == "+" or " ":
    auto_mode = True
if ask_auto_mode == "-":
    auto_mode = False
    print("")
    your_dir = input(f"{w}Введите путь к папке с картинкой/картинками.\nПример - D:/User/Img\nВведите путь: ")

if auto_mode == True:
    print("")
    print(f"{y}[Лог]Начинаю удаление фонов с картинок в режиме input...")
    i = rem_bg_def()
if auto_mode == False:
    input_dir = os.path.abspath(your_dir)
    print("")
    print(f"{y}[Лог]Начинаю удаление фонов с картинок в папке: {your_dir}...")
    i = rem_bg_def()

if i == 0: 
    print("")
    print(f"{r}[Ошибка]Чтобы удалить фон с картинки, нужна картинка.")

if i > 0:
    print("")
    print(f"{g}Готово! Удалены фоны с {i} картинок.")

print("")
input(f"{w}Чтобы выйти из скрипта нажми Enter...")