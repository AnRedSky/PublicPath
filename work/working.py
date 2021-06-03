import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
import xlrd
import xlwt

path = r'./成功易5月份人民币和香港端口日均消耗.xlsx'
# path = "*./2021-4月份谷歌消费活跃账号.csv"
sheet=['美金端口']
# df=pd.read_excel(path,sheet_name=sheet)
df=xlrd.open_workbook(path,sheet)

# df=pd.read_csv(path)

# path = "./2021-4月份谷歌消费活跃账号.csv"
# pd.read_csv(path)

pd.read_excel(path,sheet)

import re


