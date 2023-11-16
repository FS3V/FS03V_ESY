def main():

    print("Was möchten Sie tun?")
    eingabe=input("Ihre Wahl: ")

    while eingabe!="bye":
            print("Was möchten Sie tun?")
            eingabe=input("Ihre Wahl: ")

	    if(eingabe == "wurzel"):
			wurzel_n()
            
    print("Bye!")
    print("Farewell!")
if __name__ == "__main__":
    main()
