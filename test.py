import pandas as pd
import matplotlib.pyplot as plt

nums = [16, 18, 28, 13, 50, 31, 25, 22, 18, 23, 29, 38]
data = pd.Series(nums)
sorted_data = data.sort_values(ascending=True)


print(data.skew())