# coding:utf-8
import easyhistory
import pandas as pd

dict = {'399006': '创业板指', '399300': '沪深300', '399933': '中证医药', '399959': '军工指数', '399395': '国证有色', '399396': '国证食品', '399393': '国证地产', '399905': '中证500', '399005': '中小板指', '000832': '中证转债', '399934': '中证金融', 'au99': 'Au99.99'}

easyhistory.Day().init(dict.keys())
