import pandas as pd
import matplotlib.pyplot as plt

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

# Part 3
chocolate = []
vanilla = []
strawberry = []

for line in df:
    line = line.strip().split(',')
    if line[2] == "Chocolate":
        chocolate.append(float(line[3]) * float(line[4]))
    elif line[2] == "Vanilla":
        vanilla.append(float(line[3]) * float(line[4]))
    elif line[2] == "Strawberry":
        strawberry.append(float(line[3]) * float(line[4]))

sum_chocolate = sum(chocolate)
sum_vanilla = sum(vanilla)
sum_strawberry = round(sum(strawberry),2)

## code for graph ##
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
flavors = ['Chocolate', 'Vanilla', 'Strawberry']
totals = [sum_chocolate, sum_vanilla, sum_strawberry]
ax.bar(flavors,totals, color =(0.5,0.1,0.5,0.6))

afont = {'fontname':'arial black'}
bfont = {'fontname':'krungthep'}

plt.title('Cupcake Totals Per Type', fontsize=24, **afont)
plt.xlabel('Types', fontsize=16, **afont)
plt.ylabel('Invoice Totals', fontsize=16, **afont)


# plt.show()


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



