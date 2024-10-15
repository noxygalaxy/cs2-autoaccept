import pyautogui
import time
from colorama import Fore, Style
import sys
import os
import pygetwindow as gw

print(Fore.GREEN + Style.BRIGHT + """
  █████╗ ██╗   ██╗████████╗ ██████╗        █████╗  ██████╗ ██████╗███████╗██████╗ ████████╗
 ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗      ██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗╚══██╔══╝
 ███████║██║   ██║   ██║   ██║   ██║█████╗███████║██║     ██║     █████╗  ██████╔╝   ██║   
 ██╔══██║██║   ██║   ██║   ██║   ██║╚════╝██╔══██║██║     ██║     ██╔══╝  ██╔═══╝    ██║   
 ██║  ██║╚██████╔╝   ██║   ╚██████╔╝      ██║  ██║╚██████╗╚██████╗███████╗██║        ██║   
 ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝       ╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚═╝        ╚═╝   """)
print("\x1b[38;2;158;99;230m                                                               by Nooxxyyy, made with <3")

TARGET_COLOR = (54, 183, 82)
TARGET_COORDINATES = (1000, 480)

def detect_and_click(target_color, coordinates):
    time.sleep(1)
    print(Fore.WHITE + " Trying to find 'ACCEPT' button..." + Style.RESET_ALL)
    for i in range(10):
        print("")
    print("\x1b[38;2;158;99;230m https://github.com/noxygalaxy")
    print("")
    print("\x1b[38;2;158;99;230m https://github.com/noxygalaxy/cs2-autoaccept")
    while True:
        active_window = gw.getActiveWindow()

        if active_window is not None:

            if "cs2" in active_window.title.lower() or "counter-strike 2" in active_window.title.lower():
                try:
                    current_color = pyautogui.pixel(*coordinates)
                    
                    if current_color == target_color:
                        time.sleep(4)
                        pyautogui.click(*coordinates)
                        time.sleep(0.2)
                    else:
                        time.sleep(0.5)
                except Exception as e:
                    print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
                    time.sleep(5)
            else:
                time.sleep(0.1)
        
        time.sleep(2)

detect_and_click(TARGET_COLOR, TARGET_COORDINATES)