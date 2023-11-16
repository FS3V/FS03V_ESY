import square

def main():
    print("Was möchten Sie tun?")
    print("[1]Quadratische Funktion loesen")
    print("[2]Wurzel")
    eingabe=input("Ihre Wahl: ")

    while eingabe!="bye":
        if eingabe == "1":
            square()
        if eingabe == "2":
            wurzel_n()
        print("Was möchten Sie tun?")
        eingabe=input("Ihre Wahl: ")
            
    print("Bye!")
    print("Farewell!")
if __name__ == "__main__":
    main()
