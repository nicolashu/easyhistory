# coding:utf-8
import easyhistory
import pandas as pd

## 下载所有历史数据
##easyhistory.Day().init(set(['399006','399300','399986','399967','399975','399933','000823']))

## 更新到最近季度
## easyhistory.update_single_code(stock_code = '150153')

## 读取
his = easyhistory.History(dtype='W')

# MA 计算, 直接调用的 talib 的对应函数
##res = his['150153'].MA(5)


## 相关系数

dict = {'399006': '创业板指', '399300': '沪深300', '399933': '中证医药', '399959': '军工指数', '399395': '国证有色', '399396': '国证食品', '399393': '国证地产', '399905': '中证500', '399005': '中小板指', '000832': '中证转债', '399934': '中证金融', 'au99': 'Au99.99'}

def returns(code): return his[code].history.pct_change()

# codes = ['399006', 'au99']
df = pd.concat(map(returns, dict.keys()), axis=1, join='inner')
df = df.dropna()
df.columns = dict.values()

print df.corr()