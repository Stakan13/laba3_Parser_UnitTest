from Parser import Parser
import re


class CardNum:
    def __init__(self):
        __p = Parser()
        __p.connect()
        __p.to_dict()
        self.__bins_data = __p.get_parse()

    def add_data_to_file(self, file_name: str):  # user input
        number = input("Enter card number: ")
        result = self.__num_validation(number)

        if result[0]:
            with open(file_name, 'r+') as file:
                last_sym = file.readlines()[-1][-1]
                if last_sym == '\n':
                    file.write(number+'\n')
                else:
                    file.write('\n')
                    file.write(number + '\n')
            print(f'{number} - belongs to {result[1]}\n'
                  f'successfully added to file')
        else:
            print("Incorrect card number!")

    def data_from_file(self, file_name: str):  # data from file
        counter = 0
        card_numbers_from_file = []

        try:
            with open(file_name, 'r') as file:
                for line in file:
                    if self.__num_validation(line)[0]:
                        counter += 1
                        card_numbers_from_file.append(line)
        except FileNotFoundError:
            print(f'file {file_name} not found')

        print(f'find {counter} valid card numbers')

        return card_numbers_from_file

    def __num_validation(self, num) -> tuple:  # validation number
        num = re.sub(r'\s', '', num)

        for key, value in self.__bins_data.items():
            for bank_in in value[0]:
                for length in value[2]:
                    if num.startswith(bank_in) and len(num) == int(length) and re.match(r'^\d+$', num):
                        return True, key

        return False, None
