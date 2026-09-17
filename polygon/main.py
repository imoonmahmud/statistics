import numpy as np
import matplotlib.pyplot as plt

income = [32000, 46000, 85000, 25000, 93000, 63000, 52000, 39000, 75000, 59000, 81000, 98000, 26000, 115000, 43000, 25000, 69000, 108000, 88000, 71000]

bins = np.arange(20000, 130000, 20000)

# compute frequency counts per bin
freq, bin_edges = np.histogram(income, bins=bins)


# midpoints of each bin
midponts = (bin_edges[:-1] + bin_edges[1:]) / 2

# add zero-frequency points
x = np.concatenate(([midponts[0] - 20000], midponts, [midponts[-1] + 20000]))
y = np.concatenate(([0], freq, [0]))

plt.plot(x, y, marker='o', color='steelblue')
plt.fill_between(x, y, alpha=0.2, color='steelblue')
plt.title('Income Frequency Polygon')
plt.xlabel('Income')
plt.ylabel('Frequency')

plt.show()