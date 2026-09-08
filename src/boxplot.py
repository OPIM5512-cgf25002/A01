from sklearn.datasets import fetch_california_housing
import pandas as pd

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)

# Features + target as a single DataFrame
df = housing.frame

# Quick check
print(df.head())
print(df.shape)

# you can save the boxplot...
import matplotlib.pyplot as plt

# Create the boxplot for 'MedInc' using plt.boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(df['MedInc'])
plt.title('Boxplot of Median Income (MedInc)')
plt.ylabel('MedInc Value')
plt.xticks([]) # Hide x-axis ticks as there's only one boxplot
plt.tight_layout()

# Save the boxplot to a file
plt.savefig('figs/boxplot.png')
plt.close() # Close the plot to prevent it from displaying if not desired