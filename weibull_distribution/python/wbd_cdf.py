from reliability.Distributions import Weibull_Distribution
import matplotlib.pyplot as plt
import csv

with open("/Users/oleg/Desktop/weibull_distribution/ruby/test.csv",'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(row['scale'],row['shape'])
    scale = row['scale']
    shape = row['shape']

dist = Weibull_Distribution(alpha=scale, beta=shape)  # this created the distribution object
dist.CDF()

plt.show()