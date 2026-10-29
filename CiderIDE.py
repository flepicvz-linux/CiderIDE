import os



def main():
    print("welcome to CiderIDE")
    print("The fastest IDE!")
    print("(mainly cause it runs in the terminal)")
    print("ALSO MOVE ME TO YOUR PROJECT FOLDER")
    print("besides from that what would you like to do")
    print("[1] create new file")
    print("[2] create new folder")
    print("[quit] quit")
    home = input(">")



    if home == "1":
        createnewfile()

    if home == "2":
        createnewfolder()

def createnewfile():
    print("what is the name of the file you would like to create")
    filename = input(">")
    print("what would you like to write in this folder")
    file_content = input(">")

    lines = []

    while True:
        line = input()
        if line == ":q":
            break
        lines.append(line)

        file_content = "\n".join(lines)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(file_content)
    print("file created")

def createnewfolder():
    print("what would you like the name of the foler to be")
    foldername = input(">")

    os.makedirs(foldername, exist_ok=True)
    print("folder created")


main()
