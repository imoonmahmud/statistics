import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='darkgrid')
import numpy as np

scores = np.array([74, 83, 69, 95, 78, 85, 42, 98, 73, 68, 90, 85, 84, 71, 88, 52, 94])


sns.displot(scores, kde=True, rug=True)
plt.ylabel('Frequency')
plt.xlabel('Score')

plt.show()

results = {}
# at most score of 69
results['at most 69'] = np.count_nonzero(scores <= 69)

# at least score of 80
results['at least 80'] = np.count_nonzero(scores >= 80)

# score between 60 and 90
results['60 to 90'] = np.count_nonzero((60 <= scores) & (90 >= scores))

print(results)