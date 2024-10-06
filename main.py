from cn import cn
from en import en
def main():
    print("1.中文\n2.English")
    choice = int(input("选择你的语言/Select your language: "))
    if choice == 1:
        cn()
    elif choice == 2:
        en()
    

if __name__ == "__main__":
    main()