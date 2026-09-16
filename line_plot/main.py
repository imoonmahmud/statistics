import matplotlib.pyplot as plt
import numpy as np

data = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8]

# count the frequency of each unique value
unique_values, counts = np.unique(data, return_counts=True)

x_coords = []
y_coords = []
for val, count in zip(unique_values, counts):
    for i in range(1, count + 1):
        x_coords.append(val)
        y_coords.append(i)

# create the plot
plt.figure(figsize=(8, 4))
plt.scatter(x_coords, y_coords, s=200, color='royalblue', edgecolors='black', zorder=3)


# Add titles and labels
plt.title('How Many Cars They Own')
plt.xlabel('Cars')
plt.ylabel('People')

# Display the plot
plt.show()


results = {}
# Own one car?
results['own on car'] = counts[1]

# Own at least two cars?
results['at least own two cars'] = sum(counts[2:])

# Own at most three cars?
results['at most own three cars'] = sum(counts[:4])

# Own four or five cars?
results['own four or five cars'] = counts[4] + counts[5]

# How many people are living in this community?
results['living people'] = sum(counts)

# Total cars?
results['total cars'] = sum(f * c for f, c in zip(unique_values, counts))