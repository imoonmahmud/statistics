import pandas as pd
import matplotlib.pyplot as plt

nums = [16, 18, 28, 13, 50, 31, 25, 22, 18, 23, 29, 38]
data = pd.Series(nums)
sorted_data = data.sort_values(ascending=True)

q1 = sorted_data.quantile(0.25)
q3 = sorted_data.quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = sorted_data[(sorted_data < lower) | (sorted_data > upper)]


# Box and Whisker Plot
plt.boxplot(sorted_data, vert=False)
plt.title('Box Plot Example')
plt.show()