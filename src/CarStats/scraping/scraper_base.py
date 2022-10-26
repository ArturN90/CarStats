#!/usr/bin/python3

"""to update"""
from abc import ABC, abstractmethod

import re
from CarStats.log import log
from CarStats.utilites.utils import export_to_json, dump


class Scrap(ABC):
    """Base class to scrap data from otomoto"""

    def __init__(self, executable_path="./../drivers/geckodriver"):
        """ init func"""

        if not isinstance(executable_path, str):
            raise TypeError(
                "Wrong type! Please specify the geckodriver path in string."
            )
        self._path = executable_path
        self._data_bank = {}
        self._browser = None
        self._all_offers = 0
        self._used_cars = 0
        self._new_cars = 0

    @property
    def path(self):
        """Path to geckodriver"""
        return self._path

    @property
    def data_bank(self):
        """Dict with data"""
        return self._data_bank

    @property
    def all_offers(self):
        """Number of all offers"""
        return self._all_offers

    @all_offers.setter
    def all_offers(self, new):
        self._all_offers = new

    @property
    def used_cars(self):
        """Number of offers with used cars"""
        return self._used_cars

    @used_cars.setter
    def used_cars(self, new):
        self._used_cars = new

    @property
    def new_cars(self):
        """Number of offers with new cars"""
        return self._new_cars

    @new_cars.setter
    def new_cars(self, new):
        self._new_cars = new

    @property
    def browser(self):
        """Gets the otomoto page"""
        return self._browser

    @browser.setter
    def browser(self, new):
        self._browser = new

    def close_browser(self):
        """End scrap session"""
        return self.browser.close()

    @abstractmethod
    def open_browser(self):
        """Start scrap session"""

    @abstractmethod
    def load_data(self):
        """Load all possible brands"""

    @abstractmethod
    def dataset(self):
        """Scraps:
        1) All Offers (for all brands or for selected brand)
        2) Used-cars Offers (for all brands or for selected brand)
        3) New-cars Offers (for all brands or for selected brand)

        """

    @abstractmethod
    def create_data_bank(self, brands_list, amounts_list):
        """collect data"""

    @staticmethod
    def clear_strings_in_list(string, option="str"):
        """Helps clearing strings from scraped data"""

        if isinstance(string, str):
            cleared_list = []
            formated_list = []
        else:
            raise TypeError("Argument must be a string!")

        for line in string.split("\n"):
            if not line.strip():
                continue
            cleared_list.append(line.lstrip())

        for index in cleared_list:
            if option in ["str"]:
                formated_list.append(re.sub("[^a-ż^A-Ż]", " ", index).strip())
            if option in ["int"]:
                formated_list.append(re.sub("[^0-9]", "", index))

        formated_list.pop(0)
        if option in ["int"]:
            formated_list = list(map(int, formated_list))

        return formated_list

    def __call__(self, **kwargs):
        #
        # Starting!
        #
        log()
        #
        self.open_browser()
        data = self.load_data()
        name_list = Scrap.clear_strings_in_list(data)
        amounts_list = Scrap.clear_strings_in_list(data, option="int")
        # FIXME
        # self.all_offers, self.used_cars, self.new_cars = self.dataset()

        self.create_data_bank(name_list, amounts_list)
        self.close_browser()
        dump(export_to_json(self.data_bank),"scraped_data.json")

        return self.data_bank
