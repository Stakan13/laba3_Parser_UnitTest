from Parser import Parser


class CardNum:
    def __init__(self):
        __p = Parser()
        __p.connect()
        __p.to_dict()
        self.__bins_data = __p.get_parse()
        self.__card_numbers_from_file = []

    @staticmethod
    def add_data_to_file():
        number = input("Enter card number: ")

        with open('data.txt', 'a') as file:
            file.write(number+'\n')

    def data_from_file(self):
        with open("data.txt", 'r') as file:
            data_list = file.readlines()
            for i in range(len(data_list)-1):
                data_list[i] = data_list[i].strip()

            self.__card_numbers_from_file = data_list

    def __num_validation(self):
        pass
