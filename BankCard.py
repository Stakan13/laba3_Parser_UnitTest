class CardNum:
    def __init__(self):
        self.__card_numbers_from_file = []
        self.__card_numbers_from_keyboard = []

    def data_from_input(self):
        number = input("Enter card number: ")
        self.__card_numbers_from_keyboard.append(number)
        print("number successfully added to database")

    def data_from_file(self):
        with open("data.txt") as file:
            data_list = file.readlines()
            for i in range(len(data_list)-1):
                data_list[i] = data_list[i].strip()

            self.__card_numbers_from_file = data_list

    def __num_validation(self):
        pass
