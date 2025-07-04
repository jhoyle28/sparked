import time

def againcheck():
    again = input("Type 'Y' to play again, otherwise type 'N' to quit!: ")
    if again.lower() == "y":
        do()
    elif again.lower() == "n":
        exit()
    else:
        print("Not a valid response, please try again.")
        againcheck()

def do():
    print("Welcome to mindreader, this is the clever program that finds the number you are thinking of!")
    number = input("Think of a number: ")
    print("Analysing brain data")
    time.sleep(1)
    print("Reading neurons")
    time.sleep(1)
    print("Implanting brain chip")
    time.sleep(1)
    print("Annotating results")
    time.sleep(1)
    print("Collecting mind data")
    time.sleep(1)
    print("Whipping the slave")
    print("Decrypting brain chip analysis")
    time.sleep(1)
    print("Encrypting brain chip data")
    time.sleep(1)
    try:
        number = float(number)
        if number.is_integer():
            number = int(number)
        print(f"The number you were thinking of is {number}!")
    except ValueError:
        print("It appears that you didn't give a valid number.")

    time.sleep(0.3)
    againcheck()

do()
