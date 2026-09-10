import numpy as np

def count_freq(nums: list) -> list:
    sorted_data = sorted(nums)
    values = []
    frequency = []
    for i in range(len(sorted_data)):
        value = sorted_data[i]
        count = 0
        for num in sorted_data:
            if value == num:
                count += 1

        if value not in values:
            values.append(value)
            frequency.append(count)
    return values, frequency

def rel_freq(frequencies: list) -> list:
    rel_freq = []
    total = sum(frequencies)
    for frequency in frequencies:
        rel_freq.append(round(frequency/total, 2))
    return rel_freq

def cr_freq(rel_freq: list) -> list:
    cumlative_freq = [rel_freq[0]]

    try:
        for i in range(len(rel_freq)):
            cumlative_freq.append(
                round(cumlative_freq[i] + rel_freq[i+1], 2))
    except IndexError:
        pass
    return cumlative_freq



nums = np.array([2,5,3,4,7,2,5,8,3,2,2,3,2,5,5,4,8,5,2,8])
values, frequency = np.unique(nums, return_counts=True)
relative_frequency = list(map(lambda x: round(x, 2),frequency / np.sum(frequency)))
cumulative_rel_frequencies = np.cumsum(relative_frequency)
