import square
import subprocess
#import kreiszahl

def showmenu():
    print("Was möchten Sie tun?")
    print("[1]Quadratische Funktion loesen")
    print("[2]Wurzel")

def main():
    showmenu()
    eingabe=input("Ihre Wahl: ")

    while eingabe!="bye":
        if eingabe == "1":
            subprocess.run(["python3","square.py"])
        if eingabe == "2":
            subprocess.run(["python3","wurzel_n.py"])
        showmenu()
        eingabe=input("Ihre Wahl: ")
            
    print("Bye!")
    print("Farewell!")
if __name__ == "__main__":
    main()
