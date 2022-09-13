from one.stats.tools import Stats

# def main():
# car_brands = {"brand"a:["Audi","BMW"], "models": [["80","100", "a3"], ["3er", "5er", "7er"]]}
#    car_brands = {
#        "Audi": {"models": {"80", "100", "a3"}, "amounts": {"80": 10222, "100": 222}},
#        "BMW": {"models": {"3er", "5er"}, "amounts": {"3er": 90, "5er": 190}},
#        "Mercedes": {
#            "models": {"class C", "class E"},
#            "amounts": {"class C": 909, "class E": 101},
#        },
#        "Toyota": {
#            "models": {"Yaris", "Avensis"},
#            "amounts": {"Yaris": 6666, "Avensis": 4444},
#        },
#    }
#    print(top3(**car_brands))


# main()

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
#new = {"a4"}
#(car_brands["Audi"]["models"]).update(new)
#print(car_brands["Audi"]["models"])
#print(car_brands)
staty = Stats(car_brands)
#staty_ = staty(statistic = "extra")
staty_ = staty()
