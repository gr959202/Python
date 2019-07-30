import quandl
import matplotlib
import matplotlib.pyplot as plt
import pandas

quandl.ApiConfig.api_key = 'eL2xn6nNthTfUrrrY8f3'

# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call

data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL', 'MSFT', 'WMT'],
#data_aapl = quandl.get_table('WIKI/PRICES', ticker = ['AAPL'],
                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] },
                        date = { 'gte': '2015-12-31', 'lte': '2019-06-31' },
                        paginate=True)

data.head()
print(data)

new = data.set_index('date')
# use pandas pivot function to sort adj_close by tickers
clean_data = new.pivot(columns='ticker')

# check the head of the output
clean_data.head()
print(clean_data)


plt.xlabel("date")
plt.ylabel("stock price")
plt.title("Stock prices of Apple,microsoft and walmart")
plt.plot(clean_data)
plt.show()
