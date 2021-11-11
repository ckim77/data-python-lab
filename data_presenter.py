#1 and #2
df = open("CupcakeInvoices.csv")

#3
# print([line.strip() for line in df])

#4
# print([line.strip().split(',')[2] for line in df])

#5
# print([round(float(line.strip().split(',')[3]) * float(line.strip().split(',')[4]),2) for line in df])

#6
# print(round(sum([float(line.strip().split(',')[3]) * float(line.strip().split(',')[4]) for line in df]),2))

#7
df.close()


# import pandas as pd
# import matplotlib.pyplot as plt

#3
# df = pd.read_csv("Cupcakeinvoices.csv")

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



