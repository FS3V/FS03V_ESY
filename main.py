import square
import subprocess
import kreiszahl

def main():
    print("Was möchten Sie tun?")
    print("[1]Quadratische Funktion loesen")
    print("[2]Wurzel")
    eingabe=input("Ihre Wahl: ")

    while eingabe!="bye":
        if eingabe == "1":
            subprocess.run(["python3","square.py"])
        if eingabe == "2":
            subprocess.run(["python3","wurzel_n.py"])
        print("Was möchten Sie tun?")
        eingabe=input("Ihre Wahl: ")
            
    print("Bye!")
    print("Farewell!")
if __name__ == "__main__":
    main()
