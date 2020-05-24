import matplotlib.pyplot as plt
import csv


def gdpfigure():
     with open('gdp.csv','r') as file:
          csv_file = csv.reader(file)
          gdp = []
          year = []
          for row in csv_file:
               gdp.append(row[1])
               year.append(row[0])
     plt.plot (gdp)
     plt.savefig('../int/img/plot.svg', format='svg')
gdpfigure()