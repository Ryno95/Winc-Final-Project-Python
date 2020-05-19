# import random
import datetime

# ------------ Data & Global Variables ---------- #
allProducts = [
    {
        "name": "apple",
        "keeps_days": 10,
        "buy": 0.1,
        "sell": 0.7,
        "stock": 200,
        "order_size": 200,
    },
    {
        "name": "toothpaste",
        "keeps_days": 365,
        "buy": 1.80,
        "sell": 2.30,
        "stock": 100,
        "order_size": 100,
    },
]
# salesPercentage = random.randint(25, 75) / 100
openingDate = datetime.datetime(2020, 1, 1, 8)
openingTime = 8
closingTime = 22


AllProductsAllInfo = []
for product in allProducts:

    AllProductsAllInfo.append(
        {
            "name": product["name"],
            "keeps_days": product["keeps_days"],
            "buy": product["buy"],
            "sell": product["sell"],
            "stock": product["order_size"],
            "order_size": product["order_size"],
            "deliveryDate": openingDate,
            "needsReorder": None,
            "nettoSales": 0,
        }
    )


# --------------- Functions ----------- #


def sales(products):
    i = 0
    #    salesList = []
    for product in products:
        # salesPercentage = 0.2  # random.randint(25, 75) / 100
        # if product["stock"] > 0:
        # if len(salesList) < len(products):

        salesAmount = round(product["stock"] * 0.1)
        stockLeftOver = product["stock"] - salesAmount
        needsReOrder = None
        nettoSales = product["nettoSales"] + (
            salesAmount * product["sell"] - salesAmount * product["buy"]
        )
        if product["stock"] < product["order_size"] * 0.3:
            print(f"STOCK FOR {product['name']} NEEDS TO BE ORDERED!!!!")
            needsReOrder = True
        else:
            needsReOrder = False
        AllProductsAllInfo[i] = {
            "name": product["name"],
            "salesAmount": salesAmount,
            "stock": stockLeftOver,
            "sell": product["sell"],
            "buy": product["buy"],
            "order_size": product["order_size"],
            "deliveryDate": product["deliveryDate"],
            "needsReorder": needsReOrder,
            "nettoSales": nettoSales,
        }

        i += 1
    return AllProductsAllInfo


def ReOrder(products):
    for product in products:
        if product["needsReorder"]:
            product["stock"] = product["stock"] + product["order_size"]
            product["orderMade"] = True
            print(f"order for {product['name']} has been made")


def nettoIncome(products):
    netSales = []
    for product in products:
        netSales.append(product["nettoSales"])
    return netSales


def printHourlyReport(products):
    nettoIncome(AllProductsAllInfo)
    sumOfNettoSales = round(sum(nettoIncome(products)), 2)
    # print(sumOfNettoSales)
    for product in products:
        print(
            f"There is a total of {product['stock']} {product['name']} left on the shelves"
        )

    print(f"The total Netto sales for the the day is {sumOfNettoSales}EUR")


# ----------- End Result ---------- #
while openingTime < closingTime:
    if openingTime == 3:
        pass
        # ReOrder(AllProductsAllInfo)
        # print(AllProductsAllInfo)
    print(f'At {openingTime} o"Clock:')
    sales(AllProductsAllInfo)
    nettoIncome(AllProductsAllInfo)
    printHourlyReport(AllProductsAllInfo)
    openingTime += 1
ReOrder(AllProductsAllInfo)
