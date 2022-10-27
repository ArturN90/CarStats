#!/usr/bin/python3
"""docs to update"""

import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

from CarStats.scraping.scraper_base import Scrap


class ScrapBrands(Scrap):
    # pylint: disable=C0301
    """Scraps basic info from otomoto"""

    def open_browser(self):
        """Start scrap session"""
        self.browser = Firefox(executable_path=self.path)  # lub ./geckodriver.exe
        self.browser.get("https://www.otomoto.pl/osobowe")
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.browser.maximize_window()

    def load_data(self):
        """Load all possible brands"""
        wait = WebDriverWait(self.browser, 10)
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

    def create_data_bank(self, brands_list, amounts_list):

        # self._models_mean_prices = dict.fromkeys(brand_, [])

        for ind, item in enumerate(brands_list):
            self.data_bank[f"{item}"] = {"brand_offers": amounts_list[ind]}
