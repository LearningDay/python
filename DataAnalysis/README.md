* **20181106**

# 用pandas_datereader获取YAHOO finace网站中的的股票信息
```python
import pandas_datareader as pdr
start = datetime(2015,1,1)
company = ['GOOG','FB','AAPL','MSFT','AMZN']
top5 = pdr.get_data_yahoo(company,start=start)['Adj Close']
···
**股票代码**
* 'BABA'阿里巴巴
* 'VIPS'唯品会
* 'GOOG'谷歌
* 'FB'脸书
* 'AAPL'苹果
* 'MSFT'微软
* 'AMZN'亚马逊
