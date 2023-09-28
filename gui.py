import customtkinter as ctk   
from CTkMessagebox import CTkMessagebox
import os
import shutil
from clear import clear
from PIL import Image, UnidentifiedImageError
from rembg import remove
from colors import *

color_start()
clear()

root = ctk.CTk()
root.title("BgRemoverLite | v0.4.0")
root.configure(bg="#333")
root.geometry("300x160")
root.resizable(False, False)
root.iconbitmap("ico.ico")


input_dir = "input"
output_dir = "output"
current_directory = os.path.dirname(os.path.abspath(__file__))

def rem_bg_def(): 
    your_dir = your_dir_string.get()
    if your_dir == "":
        your_dir = "input"
    input_dir = os.path.abspath(your_dir)
    pics = 0
    for filename in os.listdir(input_dir):
        try:
            pics += 1

            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{filename[:-4]}_output.png")

            if not filename.endswith(".png"):
                input_image = Image.open(input_path).convert("RGB")
                input_path = os.path.join(output_dir, f"{filename[:-4]}_input.png")
                input_image.save(input_path)

            input_image = Image.open(input_path)
            output_image = remove(input_image)
            output_image.save(output_path)

        except PermissionError:
            pics -= 1
            print(f"PermissionError | Pic #{pics}")
            pass
        except FileNotFoundError:
            pics -= 1
            print(f"FileNotFoundError | Pic #{pics}")
            pass
        except UnidentifiedImageError:
            pics -= 1
            print(f"UnidentifiedImageError")
            pass
        print(f"[Debug]Input dir: {your_dir}")
    CTkMessagebox(title="Ready!", message=f"Successfully removed backgrounds from {pics} images", icon="check", option_1="Thanks!")
    return pics

input_label = ctk.CTkLabel(root, text="Pics dir:")
input_label.pack()

your_dir_string = ctk.CTkEntry(root, placeholder_text="Enter your dir...", width=250)
your_dir_string.pack()

tip1_label = ctk.CTkLabel(root, text="If you leave the «Pics dir» field empty, \nthen images from the «input» folder will be used.")
tip1_label.pack(pady=5)

button_rembg = ctk.CTkButton(root, text="START", command=rem_bg_def, fg_color="#32CD32", width=150, height=50, text_color="#000000", hover_color="#145C14")
button_rembg.pack(pady=10)

root.mainloop()

pycache_directory = os.path.join(current_directory, '__pycache__')
shutil.rmtree(pycache_directory)