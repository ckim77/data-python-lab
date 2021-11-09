import pandas as pd

#3
df = pd.read_csv("Cupcakeinvoices.csv")

# for i in df.itertuples():
#     print(i)

#4
# for row in df.itertuples():
#     print(row.Type)

#5
# for row in df.itertuples():
#     totalPrice = row.Quantity * row.Price
    # print(round(totalPrice,2))

#6
# res = []
# for row in df.itertuples():
#     totalPrice = row.Quantity * row.Price
#     res.append(totalPrice)

# print(round(sum(res),2))

#7
