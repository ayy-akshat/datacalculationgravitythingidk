import csv
import pandas as pd

df = pd.read_csv("final.csv")
data = df.to_numpy()

G = 6.6743 * (10**-11)

def gravity(mass, radius):
    return G * mass/(radius**2)

d = [["name", "distance", "mass", "radius", "gravity"]]

for index, row in enumerate(data):
    template = [row[0], row[1], row[2] * 1.989e+30, row[3] * 6.957e+8]
    mass = template[2]
    radius = template[3]
    g = gravity(mass, radius)
    template.append(g)
    d.append(template)

with open("data.csv", "w") as data_csv:
    writer = csv.writer(data_csv)
    writer.writerows(d)