#!/usr/bin/python3
import re


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from CarStats.log import log


class Scrap:
    """class to scrap data from otomoto"""

    def __init__(self, executable_path='./../drivers/geckodriver'):
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

    def open_browser(self):
        """Start scrap session"""
        self.browser = Firefox(executable_path=self.path)  # lub ./geckodriver.exe
        self.browser.get("https://www.otomoto.pl/osobowe")
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.browser.maximize_window()

    def close_browser(self):
        """End scrap session"""
        return self.browser.close()

    def load_brands(self):
        """Load all possible brands"""
        wait = WebDriverWait(self.browser, 20)
        wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div/div/div/div[2]/div[1]/form/section/div/div[2]/div/div/input",
                )
            )
        ).click()
        brands = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div/div/div/div[2]/div[1]/form/section/div/div[2]/div/ul",
                )
            )
        )
        return brands.text

    def dataset(self):
        """Scraps:
        1) All Offers (for all brands or for selected brand)
        2) Used-cars Offers (for all brands or for selected brand)
        3) New-cars Offers (for all brands or for selected brand)

        """
        browser = self.browser
        all_offers = browser.find_element("css selector", ".ooa-17fz4xg").text
        all_offers = int(re.sub("[^0-9]", "", all_offers))

        new_offers = browser.find_element(
            "css selector", "a.ooa-1fh9wzo:nth-child(3)"
        ).text
        new_offers = int(re.sub("[^0-9]", "", new_offers))

        return (all_offers, all_offers - new_offers, new_offers)

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
                formated_list.append(re.sub("[^a-z^A-Z]", " ", index).strip())
            if option in ["int"]:
                formated_list.append(re.sub("[^0-9]", "", index))

        formated_list.pop(0)
        if option in ["int"]:
            formated_list = list(map(int, formated_list))

        return formated_list

    def create_data_bank(self, brands_list, amounts_list):

        # self._models_mean_prices = dict.fromkeys(brand_, [])

        for ind, item in enumerate(brands_list):
            self.data_bank[f"{item}"] = {"brand_offers": amounts_list[ind]}

        # self.data_bank.update({"General":{"all_offers": self.all_offers}})
        # self.data_bank["General"].update({"used_cars": self.used_cars})
        # self.data_bank["General"].update({"new_cars": self.new_cars})


    def __call__(self, **kwargs):
        #
        # Starting!
        #
        log()
        #
        self.open_browser()
        brands = self.load_brands()
        brands_list = Scrap.clear_strings_in_list(brands)
        amounts_list = Scrap.clear_strings_in_list(brands, option="int")
        self.all_offers, self.used_cars, self.new_cars = self.dataset()

        self.create_data_bank(brands_list, amounts_list)
        self.close_browser()
        return self.data_bank
