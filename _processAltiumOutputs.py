import os
import shutil
import zipfile

print "Process Altium Outputs Script v1"
print "Written by Nick McComb | www.nickmccomb.net"

dirName = os.path.split(os.path.dirname(os.getcwd()))[1]

if not os.path.exists(dirName):
    os.makedirs(dirName)

PCBFileName = ""

def make_zipfile(output_filename, source_dir):
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename): # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)

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

make_zipfile(dirName + ".zip", dirName)
print "Compressed folder to " + dirName + ".zip")