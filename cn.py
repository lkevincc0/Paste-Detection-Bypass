import os
import time
from code_format import code_format
import pyautogui
def cn():
    file_path = 'code.txt'

    if not os.path.exists(file_path):
        print("未找到 code.txt 文件，请检查文件是否存在。")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        if content == "":
            return '请确保code.txt不为空'


    with open(file_path, 'r', encoding='utf-8') as file:
        user_code = file.read()

    code_lines = code_format(user_code)


    print("请在5秒内切换到输入窗口...")
    time.sleep(5)


    for line in code_lines:
        pyautogui.typewrite(eval(line))  
        pyautogui.press('enter')
        time.sleep(1)  

    print("完成！")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("")
    print(f"{file_path} 文件内容已清除。")