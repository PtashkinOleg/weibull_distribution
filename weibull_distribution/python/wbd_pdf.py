from reliability.Distributions import Weibull_Distribution
import matplotlib.pyplot as plt
import csv

with open("/Users/oleg/Desktop/ruby/test.csv",'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['scale'],row['shape'])
    src1 = row['scale']
    src2 = row['shape']

dist = Weibull_Distribution(alpha=src1, beta=src2)  # this created the distribution object
dist.PDF()

plt.show()