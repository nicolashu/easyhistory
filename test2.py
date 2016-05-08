# coding:utf-8
import easyhistory
# from easyhistory.store import CSVStore

from easyhistory import store

mystore = store.use(export='csv', path='history', dtype='D')

# result = mystore.get_factors('150153', '2015-03-25')
result = mystore.get_factors('150153', '2015-03-25')

print result