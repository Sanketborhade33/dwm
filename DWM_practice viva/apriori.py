# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

# Loading the dataset
dataset = pd.read_csv('market.csv', header=None)

# Preparing the transactions list
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])

# Applying the Apriori algorithm
rules = apriori(transactions=transactions, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2)

# Converting the results into a list
results = list(rules)

# Displaying the results in a more readable format
for rule in results:
    items = [x for x in rule.items]
    print(f"Rule: {items}")
    print(f"Support: {rule.support}")
    print(f"Confidence: {rule.ordered_statistics[0].confidence}")
    print(f"Lift: {rule.ordered_statistics[0].lift}")
    print("="*20)