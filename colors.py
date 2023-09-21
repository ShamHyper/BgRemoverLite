from colorama import Fore
from colorama import init
from colorama import just_fix_windows_console

def color_start():
    just_fix_windows_console()
    init()
    print("Colors initialized!")
    
r = Fore.RED
g = Fore.GREEN
y = Fore.YELLOW
w = Fore.WHITE