from BankCard import CardNum

c = CardNum()


def start(): # start program
    while True:
        print("1 - add card number to file\n"
              "2 - validate data from file\n"
              "3 - print data from file\n"
              "4 - exit\n")
        choice = input("Choose action: ")

        if choice == '1':
            c.add_data_to_file('data.txt')
        elif choice == '2':
            c.data_from_file('data.txt')
        elif choice == '3':
            print(c.data_from_file('data.txt'))
        elif choice == '4':
            break
        else:
            print("Incorrect choice")


if __name__ == "__main__":
    start()
