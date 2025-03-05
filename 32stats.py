import sys
import math

# compiling the inputs
nums = []
for arg in sys.argv[1:]:
    f = float(arg)
    nums.append(f)

# calculate the number of values
num_values = 0
for i in nums:
    num_values += 1
print(f'Number of values: {num_values}')

# calculate min and max
min_val = nums[0]
max_val = nums[0]
for i in nums:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i
print(f'Minimum value: {min_val}')
print(f'Maximum value: {max_val}')

# find the mean
sum = 0
for i in nums:
    sum += i
mean = sum / num_values
print(f'Mean: {mean}')

# find the standard deviation
devs = 0
for i in nums:
    devs += (i - mean) ** 2

stan_dev = math.sqrt(devs / (num_values - 1))
print(f'Standard deviation: {stan_dev:.4f}')

# calculate the median
if num_values % 2 == 0:
    median = (num_values / 2) + 1
else:
    median = (num_values + 1) / 2
print(f'Median: {median}')