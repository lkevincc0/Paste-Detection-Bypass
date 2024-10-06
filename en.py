import os
import time
from code_format import code_format
import pyautogui
def en():
    file_path = 'code.txt'

    if not os.path.exists(file_path):
        print("Cannot find code.txt, please check if it exists")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        if content == "":
            return 'please make sure code.txt is not empty'
        
    with open(file_path, 'r', encoding='utf-8') as file:
        user_code = file.read()

    code_lines = code_format(user_code)


    print("Please switch to the input window within 5 seconds...")
    time.sleep(5)


    for line in code_lines:
        pyautogui.typewrite(eval(line))  
        pyautogui.press('enter')
        time.sleep(1)  

    print("Done!")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("")
    print(f"{file_path} Erase code.txt content already")