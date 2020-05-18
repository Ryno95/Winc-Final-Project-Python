import myData

import random

# import datetime


# ------ Classes -----#
class Product:
    def __init__(self, product):
        self.product = product


class AllProducts:
    pass


class PrintHourlyReport:
    pass


class Sales:
    def __init__(self, products, salesPercentage):
        self.products = products
        self.salesPercentage = salesPercentage
        self.sales = []
        self.nettoSales = []

    def calculateSales(self):
        i = 0
        for product in self.products:
            self.products[i] = {
                "name": product["name"],
                "salesAmount": round(product["stock"] * self.salesPercentage),
                "stock": product["stock"]
                - round(product["stock"] * self.salesPercentage),
                "sell": product["sell"],
                "buy": product["buy"],
            }
            i += 1
        return self.products

    def calculateNetto(self):
        for product in self.products:
            bruto = round(product["salesAmount"] * product["sell"], 2)
            netto = bruto - (product["salesAmount"] * product["buy"])
            self.nettoSales.append(
                {
                    "name": product["name"],
                    "stock": product["stock"],
                    "bruto": bruto,
                    "netto": netto,
                }
            )
        return self.nettoSales


# ------ Global variables and data ------- #
allProducts = [myData.products[0], myData.products[1]]
AllProductsAllInfo = []
for product in allProducts:
    AllProductsAllInfo.append(
        {
            "name": product["name"],
            "keeps_days": product["keeps_days"],
            "buy": product["buy"],
            "sell": product["sell"],
            "salesAmount": 0,
            "stock": product["stock"],
            "order_size": product["order_size"],
        }
    )
# print(AllProductsAllInfo)

bussinessHours = {"open": "08", "close": "22", "hoursOpen": 4}


# --------- Sales and profit ------------ #
salesPercentage = random.randint(25, 75) / 100
x = Sales(AllProductsAllInfo, salesPercentage)
salesAmount = Sales.calculateSales(x)

# print(allProducts)
i = 1
while i < bussinessHours["hoursOpen"]:
    print(">>>>>>>>>>> List fo the sales: ", x.calculateSales())
    print(">>>>>list for the Netto: ", x.calculateNetto())
    #    print(f">>>>>> Netto Hours number :", x.calculateNetto())
    i += 1


# print(">>>>>> Sales:", Sales.calculateSales(x))
# print(">>>>>> Netto:", Sales.calculateNetto(x))
