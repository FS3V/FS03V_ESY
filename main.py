import solve_square_function

def main():

    print("Was möchten Sie tun?")
    print("[1]Quadratische Funktion loesen")
    eingabe=input("Ihre Wahl: ")

    while eingabe!="bye":
            if eingabe == "1":
                solve_square_function()
            print("Was möchten Sie tun?")
            eingabe=input("Ihre Wahl: ")

	    if(eingabe == "wurzel"):
			wurzel_n()
            
    print("Bye!")
    print("Farewell!")
if __name__ == "__main__":
    main()
