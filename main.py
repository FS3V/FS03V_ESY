import square
import subprocess
import kreiszahl
import muenze_werfen

def main():
    print("Was möchten Sie tun?")
    print("[1]Quadratische Funktion loesen")
    print("[2]Wurzel")
    print("[3]Münzwurf-Funktion")

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
        if eingabe == "3"
            muenze_werfen(["python3","muenze_werfen.py"])
        print("Was möchten Sie tun?")
        showmenu()
        eingabe=input("Ihre Wahl: ")

    print("Bye!")
    print("Farewell!")
if __name__ == "__main__":
    main()
