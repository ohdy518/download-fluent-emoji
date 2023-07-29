import requests

ERROR_INVALID_NAME = "The name of the emoji is invalid. Please check for typos and capitalization. \nQuitting..."
ERROR_INVALID_MODE = "The name of the mode is invalid. Please check for typos. \nQuitting..."
ERROR_FILE_EX = "The file you are trying to download already exists. Remove the file to download again. \nQuitting..."
SUCCESS = "Success! Download finishied successfully in .\\downloads\\ folder. "
namebase = []
modebase = ["3d", "flat", "color", "high contrast"]
with open("fname.txt", "r") as op:
    for i in op.read().split("\n"):
        namebase.append(i)

name = input("Name: ")
if name not in namebase:
    print(f"\033[1;31;40m{ERROR_INVALID_NAME}\033[0;37;40m")
    exit()
mode = input("Mode: ")
if mode.lower() not in modebase:
    print(f"\033[1;31;40m{ERROR_INVALID_MODE}\033[0;37;40m")
linkbase = "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/"
if mode.lower() == "3d":
    weblink = f"{linkbase}{name.replace(' ', '%20')}/3D/{name.replace(' ', '_').lower()}_3d.png"
if mode.lower() == "flat":
    weblink = f"{linkbase}{name.replace(' ', '%20')}/Flat/{name.replace(' ', '_').lower()}_flat.svg"
if mode.lower() == "color":
    weblink = f"{linkbase}{name.replace(' ', '%20')}/Color/{name.replace(' ', '_').lower()}_color.svg"
if mode.lower() == "high contrast":
    weblink = f"{linkbase}{name.replace(' ', '%20')}/High%20Contrast/{name.replace(' ', '_').lower()}_high_contrast.svg"
print(f"\033[1;32;40m{weblink}\033[0;37;40m")

action = input("Type (dl) to download: ")
try: 
    if action.lower() == "dl":
        if mode.lower() == "3d":
            create = open(f".\\downloads\\{name.replace(' ', '_').lower()}_3d.png", "x")
            with open(f".\\downloads\\{name.replace(' ', '_').lower()}_3d.png", "wb") as ops:
                ops.write(requests.get(weblink).content)
        else:
            create = open(f".\\downloads\\{name.replace(' ', '_').lower()}_{mode.lower()}.svg", "x")
            with open(f".\\downloads\\{name.replace(' ', '_').lower()}_{mode.lower()}.svg", "wb") as ops:
                ops.write(requests.get(weblink).content)
except FileExistsError:
    print(f"\033[1;31;40m{ERROR_FILE_EX}\033[0;37;40m")
    exit()
else:
    print(f"\033[1;32;40m{SUCCESS}\033[0;37;40m")