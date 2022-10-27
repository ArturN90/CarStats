#!/usr/bin/python3
"""
to update
"""
from functools import reduce
from CarStats.utilites.utils import check


class Stats:
    """Building the stats on Otomoto data"""

    def __init__(self, car_brands):
        """Init the Stats Class"""

        if not isinstance(car_brands, dict):
            raise TypeError("Wrong type. Dict type required.")
        self._car_brands = car_brands
        self._statistic = "basic"
        self._brands_offers = dict()
        self._models_mean_prices = dict.fromkeys(car_brands, [])
        self._archive = False
        # self._models_mean_prices = dict()
        # self._models_mean_prices = car_brands.copy()
        # print(car_brands.values())
        # print(self._models_mean_prices)

    @property
    def car_brands(self):
        """Data Bank of Cars"""
        return self._car_brands

    @property
    def statistic(self):
        """Type of analysis"""
        return self._statistic

    @statistic.setter
    def statistic(self, new):
        if new in ["basic", "extra"]:
            self._statistic = new
        else:
            self._statistic = "basic"

    @property
    def archive(self):
        """Makes a decision:
        *True: make a achrive
        *False: no adding data to archive

        """
        return self._archive

    @archive.setter
    def archive(self, new):
        self._archive = new

    @property
    def brands_offers(self):
        """Numbers of offers for the brand"""
        return self._brands_offers

    @property
    def models_mean_prices(self):
        """....."""
        return self._models_mean_prices

    # @models_mean_prices.setter
    # def models_mean_prices(self, new):
    # """....."""
    # self._models_mean_prices.update(new)

    def top3_amount(self):
        """top 3 brands with the biggest number of offers"""
        cars = self.car_brands
        for name in cars:
            total = 0
            for amount in cars[f"{name}"]:
                total += cars[f"{name}"]["brand_offers"]
            self.brands_offers[(f"{name}")] = total

        # return heapq.nlargest(3, self.brands_offers)
        return sorted(self.brands_offers, key=self.brands_offers.get, reverse=True)[:3]

    def top3_mean_prices(self):
        """top 3 models with highest mean price"""
        self.mean_prices()
        means = self.models_mean_prices
        values = {}
        for key in means.keys():
            values.update(reduce(lambda key, y: dict(key, **y), (means[f"{key}"])))
            # print(values)
        return sorted(values, key=values.get, reverse=True)[:3]

    def mean_prices(self):
        """to update"""
        cars = self.car_brands
        for name in cars:
            ratio = []
            for price in cars[f"{name}"]["prices"]:
                avv = sum((cars[f"{name}"]["prices"][f"{price}"]))
                n_o = len((cars[f"{name}"]["prices"][f"{price}"]))
                ratio.append({f"{price}": avv / n_o})

            self.models_mean_prices[f"{name}"] = ratio

    def read_and_set(self, **kwargs):
        """Reads and sets input"""
        for name in kwargs:
            check(name, name, "statistic", "archive")
        self.statistic = kwargs.get("statistic", "basic")
        self.archive = kwargs.get("archive", False)

    def base_stats(self):
        """Presents a basic statistic"""
        brands = self.top3_amount()
        print("Top 3 numbers of offers", brands)
        print("\nSpecifically...")
        print(
            brands[0], "with", self.car_brands[f"{brands[0]}"]["brand_offers"], "offers"
        )
        print(
            brands[1], "with", self.car_brands[f"{brands[1]}"]["brand_offers"], "offers"
        )
        print(
            brands[2], "with", self.car_brands[f"{brands[2]}"]["brand_offers"], "offers"
        )

    def extra_stats(self):
        """to do"""
        raise NotImplementedError

    def __call__(self, **kwargs):
        #
        # Starting!
        #
        # log()
        #
        # Read input:
        #
        self.read_and_set(**kwargs)
        if self.statistic in ["basic"]:
            print(
                "-------------------------- PRESNTING BASIC STATS -------------------------------"
            )
            self.base_stats()
            print(
                "--------------------------- END OF PRESENTATION --------------------------------"
            )
        else:
            self.extra_stats()
        if self.archive:
            print("Data is stored ...")
            raise NotImplementedError
