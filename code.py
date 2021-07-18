import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv

df = pd.read_csv("newdata.csv")
data = df["average"].tolist()

dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
standard_deviation = statistics.stdev(dataset)

print("mean:",mean)
print("standard_deviation:",standard_deviation)
