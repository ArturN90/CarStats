from CarStats.scraping.scraper import Scrap
from CarStats.stats.tools import Stats

scraping=Scrap("./geckodriver")
scrap_=scraping()

car_brands = {
    "Audi": {
        "models": {"80", "100", "a3"},
        "amounts": {"80": 10222, "100": 222, "a3": 3121},
        "prices": {
            "80": [1200, 5111, 3222],
            "100": [3344, 6777, 9999],
            "a3": [4544, 47778, 19999],
        },
    },
    "BMW": {
        "models": {"3er", "5er", "7er"},
        "amounts": {"3er": 90, "5er": 190, "7er": 9},
        "prices": {
            "3er": [10200, 51111, 63222],
            "5er": [44444, 67778, 89999],
            "7er": [467778, 889999],
        },
    },
    "Mercedes": {
        "models": {"class C", "class E"},
        "amounts": {"class C": 909, "class E": 101},
        "prices": {
            "class C": [10200, 221111, 33222],
            "class E": [144444, 167778, 289999],
        },
    },
    "Toyota": {
        "models": {"Yaris", "Avensis"},
        "amounts": {"Yaris": 6666, "Avensis": 4444},
        "prices": {"Yaris": [1000, 1111, 2222], "Avensis": [44444, 67778, 89999]},
    },
}
staty = Stats(car_brands)
staty_ = staty()

