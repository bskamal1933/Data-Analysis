# -*- coding: utf-8 -*-
"""Haberman.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12QyP26Zbz7o0YoHdcBjRoUAMeJBoyQGy

+ Exploratory data analysis (EDA) on Haberman dataset

+ Objective:
1. To clearly specify the given data accordingly.
2. To perform the statistical operations like Mean ,Median , Std Deviation, Percentile, etc.
3. To clearly represent the given data in the pictorial plots which will reduce the coplexity of classification and make our analysis easy.
"""

# from google.colab import drive
# drive.mount('/content/drive')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
import os

warnings.filterwarnings("ignore")

print(os.getcwd())

data = pd.read_csv("haberman.csv")
print(data)

"""+ Imported the data to the data variable and read the data using Pandas."""

print(data.shape)

"""+ Minimum and Maximum values of the columns data in the table."""

data.columns = ['age', 'year', 'nodes', 'status']
print('min age =', data.age.min())
print('max age =', data.age.max())
print('min year ', data.year.min())
print('max year=', data.year.max())
print('min nodes = ', data.nodes.min())
print('max nodes=', data.nodes.max())

"""+ Displaying all the data present in table according to nodes.


"""

n = data.groupby('nodes')
for n1 in n:
    print(n1)

print('data where maximum nodes =\n', data[data.nodes == data.nodes.max()])

data.describe()

print('mean of age =', data.age.mean())
print('mean of year =', data.year.mean())
print('mean of nodes =', data.nodes.mean())

print('median of age =', data.age.median())
print('median of year =', data.year.median())
print('median of nodes =', data.nodes.median())

print('standard deviation of age =', data.age.std())
print('standard deviation of year =', data.year.std())
print('standard deviation of nodes =', data.nodes.std())

print('percentile of age =', np.percentile(data['age'], np.arange(0, 100, 25)))
print('percentile of year =', np.percentile(data['year'], np.arange(0, 100, 25)))
print('percentile of nodes =', np.percentile(data['nodes'], np.arange(0, 101, 25)))

"""+ Univariate analysis"""

sns.FacetGrid(data, hue='status') \
    .map(sns.distplot, 'year') \
    .add_legend()
plt.grid()
plt.legend()
plt.title(' Univarient analysis ')
plt.show()

"""+ Pair plot for the given data to study multiple scenarios.
+ As shown in the pair plot all the points are very close to each other, hence it is very difficult to analyse the data in below predicted plots.
"""

# pair plot ( Bi-varient analysis)
sns.set_style('whitegrid')
sns.pairplot(data, hue='status') \
    .add_legend()
plt.title('Pair plot')
plt.show()

for col in data.columns:
    sns.FacetGrid(data, hue='status') \
        .map(sns.distplot, col) \
        .add_legend()

    plt.grid()
    plt.title('uni-varient')

plt.show()

"""+ Cumulative Density function (CDF) with PDF for given data is predicted below who is effected."""

plt.title('PDF & CDF of age,year and nodes')
''' data of AGE '''
counts, bin_edges = np.histogram(data['age'], bins=20, density=True)
pdf = counts / sum(counts)

# print("pdf =: ",pdf)
# print("bin edges =: ",bin_edges)

cdf = np.cumsum(pdf)

plt.plot(bin_edges[1:], pdf, label='pdf')
plt.plot(bin_edges[1:], cdf, label='cdf')
plt.xlabel('colomn')

''' data of YEAR '''
counts, bin_edges = np.histogram(data['year'], bins=20, density=True)
pdf = counts / sum(counts)
# print("pdf =: ",pdf)
# print("bin edges =: ",bin_edges)
cdf = np.cumsum(pdf)

plt.plot(bin_edges[1:], pdf, label='pdf')
plt.plot(bin_edges[1:], cdf, label='cdf')
plt.xlabel('colomn')

'''data of NODES '''

counts, bin_edges = np.histogram(data['nodes'], bins=20, density=True)
pdf = counts / sum(counts)
# print("pdf =: ",pdf)
# print("bin edges =: ",bin_edges)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label='pdf')
plt.plot(bin_edges[1:], cdf, label='cdf')
plt.xlabel('colomn')
plt.legend()
plt.show()

"""+ Below are the box plot with whiskers which gives us the clear understanding where we can differentiate the effected and non effected by using the age,year and nodes factor."""

# Box Plot with whiskers

sns.boxplot(x='status', y='age', data=data, hue='status', dodge=False)
plt.title('Box plot for age')
plt.show()
sns.boxplot(x='status', y='year', data=data, hue='status', dodge=False)
plt.title('Box plot for year')
plt.show()
sns.boxplot(x='status', y='nodes', data=data, hue='status', dodge=False)
plt.title('Box plot for nodes')
plt.show()

"""+ Below are the Violin plots for the effected people which clearly saperates the effected and non effected than box plot.
+ Because Violin plot shows the density of the effected people and non effected people which reduces the error to occur when compared to box plot.
"""

# Violin Plot

sns.violinplot(x='status', y='age', data=data, hue='status', dodge=False)
plt.title('Violin plot for age')
plt.show()
sns.violinplot(x='status', y='year', data=data, hue='status', dodge=False)
plt.title('Violin plot for year')

plt.show()
sns.violinplot(x='status', y='nodes', data=data, hue='status', dodge=False)
plt.title('Violin plot for nodes')

plt.show()

# Contour plot

sns.jointplot(x='status', y='age', data=data, kind='kde', dodge=False)
plt.title('Contour plot for age')

plt.show()
sns.jointplot(x='status', y='year', data=data, kind='kde', dodge=False)
plt.title('Contour plot for year')
plt.show()

sns.jointplot(x='status', y='nodes', data=data, kind='kde', dodge=False)
plt.title('Contour plot for nodes')
plt.show()

"""+ The above is the Contour plot which clearly shows the density of the effected area clearly than other plots.
+All the plots shows the effected area based on age, year and nodes.
"""
