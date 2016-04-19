import os
import shutil

print "Process Altium Outputs Script v1"
print "Written by Nick McComb | www.nickmccomb.net"

dirName = os.path.split(os.path.dirname(os.getcwd()))[1]

if not os.path.exists(dirName):
    os.makedirs(dirName)

PCBFileName = ""

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if f.find(".GBL", 0, len(f)) != -1:
        shutil.move(f, dirName + "/" + f)
        print "moved .GBL!"
    if f.find(".GBO", 0, len(f)) != -1:
        shutil.move(f, dirName + "/" + f)
        print "moved .GBO!"
    if f.find(".GBS", 0, len(f)) != -1:
        shutil.move(f, dirName + "/" + f)
        print "moved .GBS!"
    if f.find(".GM1", 0, len(f)) != -1:
        shutil.move(f, f.split(".", 1)[0] + ".GKO")
        print "Renamed " + f + " to " + f.split(".", 1)[0] + ".GKO"
        shutil.move(f.split(".", 1)[0] + ".GKO", dirName + "/" + f.split(".", 1)[0] + ".GKO")
        PCBFileName = f.split(".", 1)[0]
        print "moved .GKO!"
    if f.find(".GTL", 0, len(f)) != -1:
        shutil.move(f, dirName + "/" + f)
        print "moved .GTL!"
    if f.find(".GTO", 0, len(f)) != -1:
        shutil.move(f, dirName + "/" + f)
        print "moved .GTO!"
    if f.find(".GTS", 0, len(f)) != -1:
        shutil.move(f, dirName + "/" + f)
        print "moved .GTS!"
    if f.find(".TXT", 0, len(f)) != -1:
        if f.find(PCBFileName, 0, len(f) != -1):
            if f.find("-", 0, len(f)) == -1:
                shutil.move(f, f.split(".", 1)[0] + ".XLN")
                print "Renamed " + f + " to " + f.split(".", 1)[0] + ".XLN"
                shutil.move(f.split(".", 1)[0] + ".XLN", dirName + "/" + f.split(".", 1)[0] + ".XLN")
                print "moved .XLN!"