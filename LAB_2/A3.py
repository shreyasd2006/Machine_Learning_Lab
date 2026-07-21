import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
df = pd.read_excel("test.xlsx", sheet_name="IRCTC Stock Price")
price = df["Price"].to_numpy()
print(np.mean(price))
print(np.var(price))
def mean_value(x):
    return sum(x) / len(x)
def variance_value(x):
    m = mean_value(x)
    return sum((i - m) ** 2 for i in x) / len(x)
t1 = []
t2 = []
for _ in range(10):
    s = time.perf_counter()
    np.mean(price)
    np.var(price)
    e = time.perf_counter()
    t1.append(e - s)
for _ in range(10):
    s = time.perf_counter()
    mean_value(price)
    variance_value(price)
    e = time.perf_counter()
    t2.append(e - s)
print(mean_value(price))
print(variance_value(price))
print(sum(t1) / 10)
print(sum(t2) / 10)
wed = df[df["Day"] == "Wed"]["Price"]
print(wed.mean())
apr = df[df["Month"] == "Apr"]["Price"]
print(apr.mean())
loss_prob = len(list(filter(lambda x: x < 0, df["Chg%"]))) / len(df)
print(loss_prob)
wed_profit = len(df[(df["Day"] == "Wed") & (df["Chg%"] > 0)]) / len(df)
print(wed_profit)
cond = len(df[(df["Day"] == "Wed") & (df["Chg%"] > 0)]) / len(df[df["Day"] == "Wed"])
print(cond)
plt.scatter(df["Day"], df["Chg%"])
plt.xlabel("Day")
plt.ylabel("Chg%")
plt.show()