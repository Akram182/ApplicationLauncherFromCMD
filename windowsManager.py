import os
import subprocess

FileDir = "Data.txt"

programsWDir = dict()

programsQueue = []
flag = True


def Add(val):
    with open(FileDir,"a") as file:
        file.write(f"{val}\n")
    
def StartProgramms(listWPrograms):
    for prog in listWPrograms:
        subprocess.Popen(programsWDir[prog])

def FillDictionary():
    with open(FileDir,"r") as file:
        allFile =  file.read()
        strin = allFile.split("\n")[:-1:]
        print(strin)
        for i in strin:
            progN = i.split(":")
            programsWDir[f"{progN[0]}"]  = f"{progN[1]}"
    



while flag:
    uinput = input("Введите команду:")
    
    if uinput.lower() == "add":
        addFile = input("введите название файла с путем пример(VsCode:C:vscode.exe):")
        Add(addFile)
    if uinput.lower() == "check":
        FillDictionary()
        
    if uinput != None:
        for key in programsWDir:
            if(uinput.lower() == key.lower()):
                programsQueue.append(key)
    
    if uinput.lower() == "list":
        for i in programsQueue:
            print(f"{i}")
                
    if uinput.lower() == "end":
        flag = False
        StartProgramms(programsQueue)
        break
            
            




















# def Work():
#     subprocess.Popen(r"C:\Users\YodgarovInc\AppData\Local\Yandex\YandexBrowser\Application\browser.exe")
#     subprocess.Popen(r"C:\Users\YodgarovInc\AppData\Local\Programs\Microsoft VS Code\Code.exe")


    
# def Gaming():
#     print("Выберете игру")
#     print("1 - Gta V\n2 - Asseto Corsa\n3 - BeamngDrive")
#     gameChoosing = int(input())
    
#     if gameChoosing == 1 :
#         subprocess.Popen(r"E:\BeamNGdrive\BeamNG.drive.exe") #Gta V
#     elif gameChoosing == 2 :    
#         subprocess.Popen(r"F:\Assetto Corsa\AssettoCorsa.exe")#Asseto Corsa
#     elif gameChoosing == 3 :
#         print("Need To Fix")
#         #subprocess.Popen(r"")#BeamngDrive
#     else:
#         print("Error")


# def Study():
#     subprocess.Popen([r"C:\Users\YodgarovInc\AppData\Local\Yandex\YandexBrowser\Application\browser.exe","https://www.deepseek.com/"])
#     subprocess.Popen(r"C:\Users\YodgarovInc\AppData\Roaming\Telegram Desktop\Telegram.exe")



# print(f"Выберете режим работы")
# print("1 - Работа")
# print("2 - Игра")
# print("3 - Учеба")
# print("4 - Сам решу")

# choose = int(input())



# if choose ==1:
#     Work()
# elif choose ==2:
#     Gaming()
# elif choose ==3:
#     Study()
# elif choose ==4:
#     print("Ok")
# else:
#     print("Error")
    
# subprocess.Popen([r"E:\Cloudfare\general (ALT6).bat","N"])



