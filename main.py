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
        # Rememeber to replace "self.products" with product when inplementing for loop
        for product in self.products:
            self.sales.append(
                {
                    "product": product["name"],
                    "salesAmount": round(product["order_size"] * self.salesPercentage),
                    "sell": product["sell"],
                    "buy": product["buy"],
                }
            )
            return self.sales

    def calculateNetto(self):
        for sale in self.sales:
            # print(self.sales["salesAmount"])
            bruto = sale["salesAmount"] * sale["sell"]
            netto = bruto - (sale["salesAmount"] * sale["buy"])
            self.nettoSales.append(
                {"product": sale["product"], "bruto": bruto, "netto": netto}
            )
            print(sale)
        return self.nettoSales


# ------ Global variables and data ------- #
allProducts = myData.products
# oneProduct = allProducts[0]
bussinessHours = {"open": "08", "close": "22"}
# orderSize = oneProduct["order_size"]


# --------- Sales and profit ------------ #
salesPercentage = random.randint(25, 75) / 100
x = Sales(allProducts, salesPercentage)
salesAmount = Sales.calculateSales(x)
# brutoSales = salesAmount[0]["sales"] * oneProduct["sell"]
# nettoSales = brutoSales - (salesAmount[0]["sales"] * oneProduct["buy"])

# print(salesAmount[0]["sales"])
# print(oneProduct["sell"])

# print(">>>>>>>>>BRUTOSALES", brutoSales)
# print(">>>>>>>>>NETTO SALES", nettoSales)
# print(oneProduct)
print(allProducts)
print(Sales.calculateNetto(x))
# print(Sales.calculateSales(x))s
