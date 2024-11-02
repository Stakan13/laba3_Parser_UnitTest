from bs4 import BeautifulSoup
import requests


class Parser:

    def __init__(self):
        self.__url = "https://www.bincodes.com/bin-list/"
        self.__page = None
        self.__bin_dict = None
        self.__bin_list = None
        self.__result_list = []

    def connect(self):  # connect to site
        try:
            self.__page = requests.get(self.__url)
            if self.__page.status_code == 200:
                print("the connection is established")
                self.__parse_bin()
            else:
                raise ConnectionError

        except ConnectionError:
            print("Connection is failed")

    def __parse_bin(self):  # parse table from site
        soup = BeautifulSoup(self.__page.text, "lxml")
        self.__bin_list = soup.findAll('table')
        bin_str = self.__bin_list[1]
        self.__bin_list = bin_str.findAll('td')

        for elem in self.__bin_list:
            self.__result_list.append(elem.text)

        self.__info_converter(1)
        self.__info_converter(3)

    def __info_converter(self, ind: int):  # convert data

        for i in range(ind, len(self.__result_list)-(ind+1), 4):
            if self.__result_list[i].find(","):
                bin_string = str(self.__result_list[i].replace(" ", ""))
                middle_list = list(bin_string.split(","))

                full_bin_list = []
                for num in middle_list:
                    if not isinstance(num, list) and num.find('-') > 0:
                        range_list = self.__nums_range(num)
                        full_bin_list.append(range_list)
                        full_bin_list = self.__flatten_list(full_bin_list)
                    else:
                        full_bin_list.append(num)

                self.__result_list[i] = full_bin_list

    @staticmethod
    def __flatten_list(nested_list) -> list:  # merge list
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(item)
            else:
                flat_list.append(item)

        return flat_list

    @staticmethod
    def __nums_range(nums: str) -> list:  # 1-2 to 1, 2, 3
        start, end = map(int, nums.split("-"))

        numbers = range(start, end+1)

        return [str(num) for num in numbers]

    def __make_sub_arrays(self) -> list:  # combining values
        values_list = []
        temp_list = []
        counter = 0

        for i in range(1, len(self.__result_list)-1):
            if counter != 3:
                temp_list.append(self.__result_list[i])
                counter += 1
            else:
                counter = 0
                values_list.append(temp_list)
                temp_list = []

        return values_list

    def to_dict(self):  # list to dict
        keys_list = [self.__result_list[x] for x in range(0, len(self.__result_list)-1, 4)]

        values_array = self.__make_sub_arrays()

        self.__bin_dict = dict(zip(keys_list, values_array))
        self.__bin_dict["Мир"] = [['2200', '2201', '2202', '2203', '2204'], 'Yes', ['16']]

        for i in list(self.__bin_dict):
            if self.__bin_dict.get(i)[1] == 'No':
                self.__bin_dict.pop(i)

    def get_parse(self):
        return self.__bin_dict
