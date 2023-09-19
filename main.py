import os
import colorama
from rem_bg import *
from colors import *

input_dir = "input"
output_dir = "output"

clr()
colorama.init()

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