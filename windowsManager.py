




def Work():
    subprocess.Popen(r"C:\Users\YodgarovInc\AppData\Local\Yandex\YandexBrowser\Application\browser.exe")
    subprocess.Popen(r"C:\Users\YodgarovInc\AppData\Local\Programs\Microsoft VS Code\Code.exe")


    
def Gaming():
    print("Выберете игру")
    print("1 - Gta V\n2 - Asseto Corsa\n3 - BeamngDrive")
    gameChoosing = int(input())
    
    if gameChoosing == 1 :
        subprocess.Popen(r"E:\BeamNGdrive\BeamNG.drive.exe") #Gta V
    elif gameChoosing == 2 :    
        subprocess.Popen(r"F:\Assetto Corsa\AssettoCorsa.exe")#Asseto Corsa
    elif gameChoosing == 3 :
        print("Need To Fix")
        #subprocess.Popen(r"")#BeamngDrive
    else:
        print("Error")


def Study():
    subprocess.Popen([r"C:\Users\YodgarovInc\AppData\Local\Yandex\YandexBrowser\Application\browser.exe","https://www.deepseek.com/"])
    subprocess.Popen(r"C:\Users\YodgarovInc\AppData\Roaming\Telegram Desktop\Telegram.exe")



print(f"Выберете режим работы")
print("1 - Работа")
print("2 - Игра")
print("3 - Учеба")
print("4 - Сам решу")

choose = int(input())



if choose ==1:
    Work()
elif choose ==2:
    Gaming()
elif choose ==3:
    Study()
elif choose ==4:
    print("Ok")
else:
    print("Error")
    
subprocess.Popen([r"E:\Cloudfare\general (ALT6).bat","N"])



