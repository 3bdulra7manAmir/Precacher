#  reads directory files names and store it without extension then write the result into a file called temp.txt
import os
from datetime import datetime
import time
import subprocess as sp

targetedPath = input("Go ahead Alpha!: ")
print("Your Path is : " + targetedPath)
fileName = input("precache file name: ")
print("Your precache file name is : " + fileName)

programName = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"

com = os.listdir(targetedPath)
counter = 0

for x in os.listdir(targetedPath):
    for x in os.listdir(targetedPath):
        if x.endswith(".xmodel_export"):
            f = open(""f"{fileName}.txt", "a")
            f.write("precachemodel("f"\"{x.split('.')[0]}\""");" + "\n")
            f.close()
            print("precachemodel("f"\"{x.split('.')[0]}\""");")
            counter = counter + 1
            if counter == len(com):
                sp.Popen([programName, f"{fileName}.csv"])

        elif x.endswith(".json"):
            f = open(""f"{fileName}.txt", "a")
            f.write("precacheitem("f"\"{x.split('.')[0]}\""");" + "\n")
            f.close()
            print("precacheitem("f"\"{x.split('.')[0]}\""");")
            counter = counter + 1
            if counter == len(com):
                sp.Popen([programName, f"{fileName}.csv"])

current_dateTime = datetime.now()
print("Finished!...")
time.sleep(3)
