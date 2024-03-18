import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
categories = data['whoAmI'].unique()
one_hot_encoded = pd.DataFrame(0, columns=categories, index=range(len(data)))
for i, category in enumerate(categories):
    one_hot_encoded[category] = (data['whoAmI'] == category).astype(int)
data = pd.concat([data, one_hot_encoded], axis=1).drop(columns=['whoAmI'])
print(data.head())
