import pandas as pd

data = pd.Series([10,11,11,22,33], name="values")
mata = pd.Series([2,3,5,8], name="values")
result = data * mata
print(result)