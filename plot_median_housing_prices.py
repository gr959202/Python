import pandas as pd
import quandl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

quandl.ApiConfig.api_key = '<YOUR AUTH TOKEN>'
data = quandl.get(["ZILLOW/C36164_SP","ZILLOW/C36447_SP"], authtoken=<YOUR AUTH TOKEN>)
print(data.head())
data.plot()
plt.legend(['San Jose', 'Berkeley'])
plt.xlabel("Year")
plt.ylabel("Housing-Price")
plt.title("Housing prices in San Jose and  berkeley for the last 10 years")
plt.show()
